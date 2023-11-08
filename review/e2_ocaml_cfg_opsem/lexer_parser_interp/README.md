# OCamlThon

**OCamlthon** is a very original (and strongly typed!) programming language. It supports two types of values:

```ocaml
type value =
| Int of int   (* 1,2,3,4,5,... *)
| Bool of bool (* true | false  *)
```

People who code in **OCamlThon** really like subtraction and division. Don't ask why. _They've also never heard of addition or multiplication._

**OCamlThon** also supports some very primitive boolean operations (`and / or`), as well as OCaml-like `if .. then .. else` statements.

Here's the CFG for **OCamlThon**:

```ocaml
Expr -> If | Or
If -> if Expr then Expr else Expr
Or -> And or Or | And
And -> Sub and And | Sub
Sub -> Div - Sub | Div
Div -> Prim / Div | Prim
Prim -> <int> | true | false | ( Expr )
```

Commented:

```ocaml
Expr -> If | Or

(* boolean operations *)
If -> if Expr then Expr else Expr
Or -> And or Or | And
And -> Sub and And | Sub

(* integer operations *)
Sub -> Div - Sub | Div
Div -> Prim / Div | Prim

(* primitive types *)
Prim -> <int> | true | false | ( Expr )
```

## Usage

- Source code is under [`src`](./src)
- Run `dune utop src` to play around with the lexer/parser/interpreter
- Questions are in [`QUESTIONS.md`](./QUESTIONS.md)
- Solutions are in [`SOLUTION.md`](./SOLUTION.md)
