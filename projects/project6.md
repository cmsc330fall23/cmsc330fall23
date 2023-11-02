# Project 6: Lambda Calc Interpreter
Due: November 15th, 2023 at 11:59 pm

Points: 35 public, 65 semipublic

FAQ: [@1435](https://piazza.com/class/lkimk0rc39wfi/post/1435)

## Introduction

In Project 6 you will implement an interpreter for Lambda calculus and an English-to-Lambda Calculus compiler.
These both consist of three components: a lexer (tokenizer), a parser, and evaluator (interpreter) or generator (compiler).

Your lexer function will convert an input string to a token list, your parser function will consume these tokens to produce an abstract symbol tree (AST), your evaluator will reduce the lambda calculus expression and your compiler will convert from one language to another.

Here is an example call to the lexer, parser, evaluator and generator.

```ocaml
let toks = lex_lambda "((Lx. x) a)" in
let ast = parse_lambda toks in
let value = reduce [] ast in value
let lambda_calc = convert (parse_engl (lex_engl "true"))
``` 

```ocaml
assert_equal toks [Lambda_LParen; Lambda_LParen; Lambda_Lambda; Lambda_Var "x"; Lambda_Dot; Lambda_Var "x"; Lambda_RParen; Lambda_Var "a"; Lambda_RParen; Lambda_EOF]
assert_equal ast  (Application (Func ("x" Var "x"), Var "a"))
assert_equal value (Var "a")
assert_equal lambda_calc "(Lx.(Ly.x))"
```

### Ground Rules

You cannot use any imperative features.
This includes things like references, mutable records, and arrays. 
Functions given in lecture/discussion will probably need to be modified for this project. 

In addition, you may ***only*** use the `Str` and `String` modules. `stdlib` functions like cons(`::`) and `^` are allowed, but `stdlib` modules like `List` are not allowed with the exception of `List.map`, `List.fold_left`, and `List.fold_right`.
No other modules will be allowed. 

### Testing & Submitting

First, make sure all your changes are pushed to Github using the `git add`, `git commit`, and `git push` commands.

Next, to submit your project, you can run `submit` from your project directory.

The `submit` command will pull your code from GitHub, not your local files. If you do not push your changes to GitHub, they will not be uploaded to gradescope.

You can test your project directly by running `dune utop src` in the project-6 directory. The necessary functions and types will automatically be imported for you.

You can write your own tests and place them in `test/student/student.ml`.

## Part 1: The Lexer (aka Scanner or Tokenizer)

Your parser will take as input a list of tokens; This list is produced by the *lexer* (also called a *scanner* or *tokenizer*) as a result of processing the input string. Lexing is readily implemented by the use of regular expressions, as demonstrated during lecture. Information about OCaml's regular expressions library can be found in the [`Str` module documentation][str doc]. You aren't required to use it, but you may find it helpful.

Your lexer must be written in [lexer.ml](./src/lexer.ml). You will need to implement the following functions: 

#### `lex_lambda`

- **Type:** `string -> lambda_token list` 
- **Description:** Converts a lambda calc expression (given as a string) to a corresponding token list using the `lambda_token` types.
- **Exceptions:** `raise (Failure "tokenizing failed")` if the input contains characters which cannot be represented by the tokens.
- **Examples:**
  ```ocaml
  lex_lambda "L" = [Lambda_Lambda; Lambda_EOF]

  lex_lambda "(Lx. (x x))" = [Lambda_LParen; Lambda_Lambda; Lambda_Var "x"; Lambda_Dot; Lambda_LParen; Lambda_Var "x"; Lambda_Var "x"; Lambda_RParen; Lambda_RParen; Lambda_EOF]

  lex_lambda ".. L aL." = [Lambda_Dot; Lambda_Dot; Lambda_Lambda; Lambda_Var "a"; Lambda_Lambda; Lambda_Dot; Lambda_EOF]

  lex_lambda "$" (* raises Failure because $ is not a valid token*)

  lex_lambda "" = [Lambda_EOF]
  ```

The `lambda_token` type is defined in [lccTypes.ml](./src/lccTypes.ml). Here's a list of tokens and their respective lexical representations:

Lexical Representation | Token Name
--- | ---
`(` | `Lambda_LParen`
`)` | `Lambda_RParen`
`.` | `Lambda_Dot`
`[a-z]` | `Lambda_Var`
`L` | `Lambda_Lambda`
`end of string` | `Lambda_EOF`
`_` | `raise (Failure "tokenizing failed")`

#### `lex_engl`

- **Type:** `string -> engl_token list` 
- **Description:** Converts an English expression (given as a string) to a corresponding token list using the `engl_token` types.
- **Exceptions:** `raise (Failure "tokenizing failed")` if the input contains characters which cannot be represented by the tokens.
- **Examples:**
  ```ocaml
  lex_engl "true" = [Engl_True; Engl_EOF]

  lex_engl "if true then false else true" = [Engl_If; Engl_True; Engl_Then; Engl_False; Engl_Else; Engl_True; Engl_EOF]

  lex_engl "true if else" = [Engl_True; Engl_If; Engl_Else; Engl_EOF]

  lex_engl "$" (* raises Failure because $ is not a valid token*)

  lex_engl "" = [Engl_EOF]
  ```

The `engl_token` type is defined in [lccTypes.ml](./src/lccTypes.ml). Here's a list of tokens and their respective lexical representations:

Lexical Representation | Token Name
--- | ---
`(` | `Engl_LParen`
`)` | `Engl_RParen`
`true` | `Engl_True`
`false` | `Engl_False`
`if` | `Engl_If`
`then` | `Engl_Then`
`else` | `Engl_Else`
`and` | `Engl_And`
`or` | `Engl_Or`
`not` | `Engl_Not`
`end of string` | `Engl_EOF`
`_` | `raise (Failure "tokenizing failed")`

### **Important Notes:**
- The lexer input is **case-sensitive**.
  - The Lambda Calc string "L" should not be lexed as `[Lambda_Var "L"]`, but as `[Lambda_Lambda]`
  - The Lambda Calc string "l" should not be lexed as `[Lambda_Lambda]` but as `[Lambda_Var "l"]`.
- Lambda Calc Variables will always be **one** character long
- Tokens can be separated by arbitrary amounts of whitespace, which your lexer should discard. Spaces, tabs ('\t'), and newlines ('\n') are all considered whitespace.
  - This means the Lambda Calc string "xx" would be `[Lambda_Var("x");Lambda_Var("x")]`
  - This means the English string "ifthenelse" would be `[Engl_If;Engl_Then;Engl_Else]`
- The last token in a token list should always be the `EOF` token. 
- When escaping characters with `\` within OCaml strings/regexp, you must use `\\` to escape from both the string and the regexp.
- Your lexing code will feed the tokens into your parser, so a broken lexer can cause you to fail tests related to parsing. 

## Part 2: The Parser

In this part, you will implement the parser part of your project. You have two functions to implement here. The parser being created will be a LL(1) parser. 
First `parse_lambda`, which takes a list of `lambda_token`s and outputs an AST for the input expression of type `lambda_ast`. 
Second `parse_engl`, which takes a list of `engl_token`s and outputs an AST for the input expression of type `engl_ast`. 
Put all of your parser code in [parser.ml](./src/parser.ml) in accordance with the signature found in [parser.mli](./src/parser.mli). 

We first offer an overview of these functions, and then we discuss the AST and Grammar for them both.

### `parse_lambda`
- **Type:** `lambda_token list -> expr`
- **Description:** Takes a list of tokens and returns an AST representing the expression corresponding to the given tokens. Use the CFG below to make your AST.
- **Exceptions:** `raise (Failure "parsing failed")` if the input fails to parse i.e does not match the expressions grammar.
- **Examples** (more below):
  ```ocaml
  parse_lambda [Lambda_Var "a"; Lambda_EOF] = (Var "a")

  (* lex_lambda "(((Lx. (x x)) a) b)" *)
  parse_lambda [Lambda_LParen; Lambda_LParen; Lambda_LParen;Lambda_Lambda; Lambda_Var "x"; Lambda_Dot; Lambda_LParen; Lambda_Var "x"; Lambda_Var "x"; Lambda_RParen; Lambda_RParen; Lambda_Var "a"; Lambda_RParen; Lambda_Var "b"; Lambda_RParen; Lambda_EOF] = 
  (Application (Application (Func ("x", Application (Var "x", Var "x")), Var "a"),Var "b"))

  parse_lambda [] (* raises Failure *)

  parse_lambda [Lambda_EOF] (* raises Failure *)

  (* lex_lambda "Lx. x" *)
  parse_lambda [Lambda_Lambda; Lambda_Var "x"; Lambda_Dot; Lambda_Var "x"; Lambda_EOF]  (* raises Failure because missing parenthesis *)
  ```

### `parse_engl`
- **Type:** `engl_token list -> engl_ast`
- **Description:** Takes a list of `engl_token` and returns an AST representing the expression corresponding to the given tokens.
- **Exceptions:** `raise (Failure "parsing failed")` if the input fails to parse i.e does not match the expressions grammar.
- **Examples**
  ```ocaml
  parse_engl [Engl_True; Engl_EOF] = (Bool true)

  (* lex_engl "if true then false else true" *)
  parse_engl [Engl_If; Engl_True; Engl_Then; Engl_False; Engl_Else; Engl_True; Engl_EOF] = 
  If (Bool true, Bool false, Bool true)

  parse_engl [] (* raises Failure *)

  parse_engl [Engl_EOF] (* raises failure *)

  (* lex_engl "true and (false or true" *)
  parse_engl [Engl_True; Engl_And; Engl_LParen; Engl_False; Engl_Or; Engl_True; Engl_EOF]  (* raises Failure because missing parenthesis *)
  ```

We have included two helpers here: `match-token` and `lookahead`. 
These functions are to help you consume and check the first token in the list and see what the next token in the list is respectively.
For example:
```ocaml
let tok_list = [Engl_LParen; Engl_True; Engl_RParen] in
assert_equal Engl_LParen (lookahead tok_list);
assert_equal [Engl_True;Engl_RParen] (match_token tok_list Engl_LParen);
(match_token tok_list Engl_RParen) (* raises error *)
```

### AST and Grammar for `parse_lambda`

Below is the AST type `lambda_ast`, which is returned by `parse_lambda`.

```ocaml
type var = string

type lambda_ast = 
  | Var of var
  | Func of var * lambda_ast 
  | Application of lambda_ast * lambda_ast
```

In the grammar given below, the syntax matching tokens (lexical representation) is used instead of the token name. For example, the grammar below will use `(` instead of `Lambda_LParen`. 

The grammar is as follows, `x` is any lowercase letter:

```text
e -> x
   | (Lx.e)
   | (e e)
```


### AST and Grammar for `parse_engl`

Below is the AST type `engl_ast`, which is returned by `parse_engl`.

```ocaml
type engl_ast= 
  | If of engl_ast * engl_ast * engl_ast
  | Not of engl_ast
  | And of engl_ast * engl_ast
  | Or of engl_ast * engl_ast
  | Bool of bool
```

In the grammar given below, the syntax matching tokens (lexical representation) is used instead of the token name. For example, the grammar below will use `(` instead of `Engl_LParen`. 

```text
  C -> if C then C else C|H
  H -> U and H|U or H|U
  U -> not U|M
  M -> true|false|(C)
```
Note that for simplicity, `and` + `or` have the same precedence in our grammar.
Due to the fact we are making a left-leaning parser, this means that whichever operation
comes first will have the least precedence.
Consider the following derivation:
```text
true and false or true
C -> H 
  -> U and H 
  -> M and H 
  -> true and H 
  -> true and U or H
  -> true and M or H
  -> true and false or H
  -> true and false or U
  -> true and false or M
  -> true and false or true
```

### **Important Notes:**
- Most tests involving the parser use the lexer first
  - eg. `assert_equal ast (parse (lex input))`
- `lookahead` and `match_token` may help reduce the number of nested `match` statements you need, but they are optional to use.

## Part 3: The Evaluator

The evaluator will consist of six (6) functions, all of which demonstrate properties of an interpreter or compiler. 
The first four functions are related to an interpreter and are `isalpha`, `reduce`, `laze`, and `eager`. 
All of these functions will be implemented in the `eval.ml` file located in [eval.ml](./src/eval.ml).

### Interpreter
#### `environment`

The `environment` type given in [lccTypes.ml](./src/lccTypes.ml) is defined as below:

```ocaml
type environment = (var * lambda_ast option) list
```

This is used to store variables and its corresponding value in the scope. For example in the environment `[("x", Some(Var("y")))]` the variable `x` has the value `Var("y")` within this scope. 

To help with this, we give a `lookup` function that takes in an `environment` and a `var` and returns what `var` is bound to (or `None` if needed (eg. free variables)).

For example, if we wanted to evaluate "let x = 3 in x + 1", then we probably want to evaluate "x + 1" where "x = 3".
In this case, we would want to call `eval [("x",Some(3)] "x + 1"`.
Consider how this would change for our project.

To make things simpler, you can assume that any intial call to `reduce`, `eager` and `laze` will always include the empty environment.

#### `isalpha`
- **Type:** `lambda_ast -> lambda_ast -> bool` 
- **Description:** Returns true if the two inputs are alpha equivalent to each other, false otherwise. `fresh()` might prove to be useful here.
- **Examples:**
  ```ocaml
  (* x, x *)
  isalpha (Var("x")) (Var("x")) = true

  (* y, x *)
  isalpha (Var("y")) (Var("x")) = false 

  (* Lx.x, Ly.y *)
  isalpha (Func("x",Var("x"))) (Func("y",Var("y"))) = true
  ```
  
#### `reduce`

- **Type:** `environment -> lambda_ast -> lambda_ast` 
- **Description:** Reduces a lambda calc expression down to beta normal form. 
- **Examples:**
  ```ocaml
  (* x = x*)
  reduce [] (Var("x")) = Var("x")

  (* Lx.(x y) = Lx.(x y)*)
  reduce [] (Func("x", Application(Var("x"), Var("y")))) = Func("x", Application(Var("x"), Var("y")))

  (* (Lx.x) y = y*)
  reduce [] (Application(Func("x", Var("x")), Var("y"))) = Var("y")
  
  (* ((Lx.x) (y ((Lx.x) b))) = y*)
  reduce [] (Application (Func ("x", Var "x"),
                        Application (Var "y", 
                                    Application (Func ("x", Var "x"), 
                                                 Var "b"))))
            = Application(Var("y"),Var("b"))
  
  (* (a ((Lb.b) y)) = a y*)
  reduce [] (Application (Var("a"), Application (Func ("b", Var("b")), Var("y")))) = Application(Var("a"),Var("y"))

  (* (Lx.x) y with environment [("y", Some(Var("z")))] => z*)
  reduce [("y", Some(Var("z")))] (Application(Func("x", Var("x")), Var("y"))) = Var("z")
  ```


#### `laze`

- **Type:** `environment -> lambda_ast -> lambda_ast` 
- **Description:** Performs a **single** beta reduction using the lazy precedence. You **do not** have to worry about ambiguous applications (see *Important Notes* below for more info).
- **Examples:**
  ```ocaml
  (* x = x*)
  laze [] (Var("x")) = Var("x")

  (* (Lx.x) y = y *)
  laze [] (Application(Func("x", Var("x")), Var("y"))) = Var("y")

  (* (Lx.x) ((Ly.y) z) = ((Ly.y) z)*)
  laze [] (Application(Func("x", Var("x")), Application(Func("y", Var("y")), Var("z")))) = Application(Func("y", Var("y")), Var("z"))

  (* ((Lx.x) (y ((Lx.x) b))) = (y ((Lx.x) b)) *)
  laze [] (Application (Func ("x", Var "x"),
                        Application (Var "y", 
                                    Application (Func ("x", Var "x"), 
                                                 Var "b"))))
            = Application (Var "y", Application (Func ("x", Var "x"), Var "b"))
  
  (* (a ((Lb.b) y)) = a y*)
  laze [] (Application (Var("a"), Application (Func ("b", Var("b")), Var("y")))) = Application(Var("a"),Var("y"))

  (* (Lx.x) ((Ly.y) z) with environment [("z", Some(Var("f")))] = ((Ly.y) z)*)
  laze [("z", Some(Var("f")))] (Application(Func("x", Var("x")), Application(Func("y", Var("y")), Var("z")))) = Application(Func("y", Var("y")), Var("z"))
  ```

  
#### `eager`

- **Type:** `environment -> lambda_ast -> lambda_ast` 
- **Description:** Performs a **single** beta reduction using the eager precedence. You **do not** have to worry about ambiguous applications (see *Important Notes* below for more info).
- **Examples:**
  ```ocaml
  (* x = x *)
  eager [] (Var("x")) = Var("x")

  (* (Lx.x) y = y *)
  eager [] (Application(Func("x", Var("x")), Var("y"))) = Var("y")

  (* ((Lx.x) ((Ly.y) z)) = (Lx.x) z *)
  eager [] (Application(Func("x", Var("x")), Application(Func("y", Var("y")), Var("z")))) = Application(Func("x", Var("x")), Var("z"))

  (* ((Lx.x) (y ((Lx.x) b))) = ((Lx.x) (y b)) *)
  eager [] (Application (Func ("x", Var "x"),
                        Application (Var "y", 
                                    Application (Func ("x", Var "x"), 
                                                 Var "b"))))
            = Application (Func("x",Var("x")),Application(Var("y"),Var("b")))
  
  (* (a ((Lb.b) y)) = a y*)
  eager [] (Application (Var("a"), Application (Func ("b", Var("b")), Var("y")))) = Application(Var("a"),Var("y"))

  (* (Lx.x) ((Ly.y) z) with environment [("z", Some(Var("f")))] = (Lx.x) ((Ly.y) f)*)
  eager [("z", Some(Var("f")))] (Application(Func("x", Var("x")), Application(Func("y", Var("y")), Var("z")))) = Application(Func("x", Var("x")), Application(Func("y",Var("y")),Var("f")))

  (* ((Ly.y) ((Lz.(Lu.u) z))) = ((Ly.y) (Lz.z)) *)
  (* refer to Important Notes section for explanation *)
  eager [] (Application(Func("y", Var("y")), Func("z", Application(Func("u", Var("u")), Var("z"))))) = Application(Func("y", Var("y")), Func("z", Var("z")))

  (* ((Lx.((Ly.y) x)) ((Lx.((Lz.z) x)) y)) = (Lx.((Ly.y) x)) ((Lz.z) y) *)
  eager [] (Application(Func("x", Application(Func("y", Var("y")), Var("x"))), Application(Func("x", Application(Func("z", Var("z")), Var("x"))), Var("y")))) = Application(Func("x", Application(Func("y", Var("y")), Var("x"))), Application(Func("z", Var("z")), Var("y")))
  ```
### **Important Notes:**
- For `eager`, there is an ambiguous case where the argument of the outermost application is not an application itself but may contain an inner application. For example: `((Ly.y) ((Lz.(Lu.u) z)))` could reduce two ways:
    - `(Lz.(Lu.u) z)` -> we say that the argument itself is a Func, thus we cannot reduce the argument further
    - `((Ly.y) (Lz.z))` -> we say that we can reduce the inner application of the argument
    - **For this project, you should implement the second way**
      - More on this here: [@1444](https://piazza.com/class/lkimk0rc39wfi/post/1444)
- For expressions with nested lambdas and arguments, `laze` and `eager` should perform a beta reduction on the outermost expression first.
  - For an expression like `((Lx.((Ly.y) b)) ((Lz.z) c))`
  - `laze` should produce `((Ly.y) b)`
  - `eager` should produce `((Lx.((Ly.y) b)) (c))`
  - `reduce` should produce `b`
- For `laze` and `eager`, you will not have to worry about ambiguous application.
  - Ambiguous means expressions where you don't know which one to reduce down first: `((a ((Lx.x) b)) (c ((Ly.y) d)))`
    - could be `((a ((Lx.x) b)) (c d)`
    - could be `((a b) (c ((Ly.y) d)))`
  - Ultimately these will reduce down to the same Beta Normal form (so you do have to worry about this for `reduce`).
- We have included `fresh` to help with `isalpha`. You do not have to use this, but we think it may be helpful.
  It is up to you to decide how/if you want to use it.
- We have included a header for a function called `alpha_convert` which **we highly recommend that you implement**. 
  The purpose would be to make every set of bound variables unique. See below for examples.
  - As shown in the parser and lexer, a variable in Lambda calculus is a single character long. 
    The type however is `string` if you want to modify this to help you with `alpha_convert`.
  - `fresh` may also help here but you do not need to use it.
- Here are some examples of `alpha_convert`. This is not the only output that would be valid:
  ```ocaml
  alpha_convert (Func("x",Var("x"))) = Func("y",Var("y"))

  alpha_convert (Func("x",Var("y"))) = Func("x",Var("y"))

  alpha_convert (Application(Func("x",Var("x")),Var("x"))) = Application(Func("y",Var("y")),Var("x"))
  ```

### Compiler

The next two functions (`convert`, and `readable`) are related to a compiler. 
Both of these functions will be implemented in the `eval.ml` file located in [eval.ml](./src/eval.ml).
`convert` will compile English to Lambda Calculus while `readable` will compile Lambda Calculus to English.
The conversion will be based upon the following Church Encodings.

English | Church Encoding 
--- | ---
`true` | `(Lx.(Ly.x))`
`false` | `(Lx.(Ly.y))`
`if a then b else c` | `((a b) c)`
`not a` | `((Lx.((x (Lx.(Ly.y))) (Lx.(Ly.x)))) a)`
`a and b` | `(((Lx.(Ly.((x y) (Lx.(Ly.y))))) a) b)`
`a or b` | `"(((Lx.(Ly.((x (Lx.(Ly.x))) y))) a) b)`

### `convert`
- **Type:** `engl_ast -> string`
- **Description:** Takes an AST and produces the lambda calculus equivalent of the expression. The resulting string should have parenthesis denoting *left association* and parenthesis around the *expression as a whole*. This will follow the Grammar given in part 2 of this project.
- **Examples** 
  ```ocaml
  convert (Bool true) = "(Lx.(Ly.x))"

  convert (If (Bool true, Bool false, Bool true)) = "(((Lx.(Ly.x)) (Lx.(Ly.y))) (Lx.(Ly.x)))"

  convert (And (Bool true, Bool false)) = "(((Lx.(Ly.((x y) (Lx.(Ly.y))))) (Lx.(Ly.x))) (Lx.(Ly.y)))"
  ```
### `readable` 
- **Type:** `lambda_ast -> string`
- **Description:** Takes an AST and produces the OCaml equivalent of the expression. The expressions may be alpha equivalent to the encodings above. Parenthesis should be around each expression: (eg. `(if a then b else c)`). See below for more information.
- **Assumptions:** You may assume that the `lambda_ast` can be encoded using the above encodings. (eg. You will not be given something like `(Func("x",Var("y")))` since this is not a valid encoding)
- **Examples** 
  ```ocaml
  readable (Func("x", Func("y", Var("x")))) = "true"

  readable (Func("y", Func("x", Var("y")))) = "true"

  let c1 = parse_lambda (lex_lambda "(((Lx.(Ly.x)) (Lx.(Ly.y)))(Lx.(Ly.x)))") in 
  readable c1 = "(if true then false else true)"

  let c2 = parse_lambda (lex_lambda "(((Lx.(Ly.((x y) (Lx.(Ly.y)))))(Lx.(Ly.x)))(Lx.(Ly.y)))")
  readable c2 = "(false and true)" 
  ```
Below are the rules for spacing and parenthesis
+ Bools
  + Bools have no surrounding whitespace and no parenthesis
  + `true`, `false`
+ If expressions
  + Have 1 set of parenthesis around it 
  + 1 space separating keywords from each other.
  + No surrounding whitespace
  + `(if true then false else true)`
+ and expressions
  + Have 1 set of parenthesis around it 
  + 1 space between the `and` keyword and the arguments.
  + No surrounding whitespace
  + `(true and false)`
+ or expressions
  + Have 1 set of parenthesis around it 
  + 1 space between the `or` keyword and the arguments.
  + No surrounding whitespace
  + `(true or false)`
+ not expressions
  + Have 1 set of parenthesis around it 
  + 1 space separating not from argument.
  + No surrounding whitespace
  + `(not true)`
+ Nested Expressions
  + follow the above rules
  + `((if (not true) then (false and true) else true) or false)`


### **Important Notes:**
- Most tests involving these functions depend on your lexer and parser
  - eg. `assert_equal value (reduce parse (lex input))`
  - eg. `assert_equal lambda_calc (convert parse (lex input))`
  - eg. `assert_equal english (readable parse (lex input))`
- As noted in the description of `convert`, The output of `convert` should be valid to send into `lex_lambda` 
  - eg. `assert_equal "true" (readable (reduce (parse_lambda (lex_lambda (convert (parse_engl (lex_engl "not false"))))))))`


## Academic Integrity

Please **carefully read** the academic honesty section of the course syllabus. Academic dishonesty includes posting this project and its solution online like a public github repo. **Any evidence** of impermissible cooperation on projects, use of disallowed materials or resources, or unauthorized use of computer accounts, **will be** submitted to the Student Honor Council, which could result in an XF for the course, or suspension or expulsion from the University. Be sure you understand what you are and what you are not permitted to do in regards to academic integrity when it comes to project assignments. These policies apply to all students, and the Student Honor Council does not consider lack of knowledge of the policies to be a defense for violating them. Full information is found in the course syllabus, which you should review before starting.

[str doc]: https://caml.inria.fr/pub/docs/manual-ocaml/libref/Str.html
