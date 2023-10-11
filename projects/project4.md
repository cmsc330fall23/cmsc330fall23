# Project 4: OCaml Warmup

Due: October 15, 2023 at 11:59 PM

Points: 50 public, 40 semipublic, 10 secret

**This is an individual assignment. You must work on this project alone.**

## Introduction

The goal of this project is to get you familiar with programming in OCaml. You will have to write a number of small functions, each of which is specified in four sections below.

We recommend you get started right away, going from top to bottom. The problems get increasingly more challenging, and in some cases later problems can take advantage of earlier solutions.

### Ground Rules

In your code, you may **only** use library functions found in the [`Stdlib` module](https://caml.inria.fr/pub/docs/manual-ocaml/libref/Stdlib.html) and the `@` operator. (This means you may **not** use the `List` module!) You may **not** use any imperative structures of OCaml such as references.

### Testing & Submitting

You should test your project three different ways in the following order:

1. Test locally using the provided public tests
2. Submit to Gradescope to see whether you're passing or failing the semipublics.
3. Write student tests to best predict what you think the secret tests are.

Running the public tests locally can by done using the command below:

`dune runtest -f`. This will run both public and student tests. If you want to only test a specific file, say your student tests file, run `dune runtest test/student`, replacing the path if your testing files are located in a directory elsewhere. We recommend you write student tests in `test/student/student.ml`.

Before you submit to Gradescope, make sure you have no warnings when running your tests. Warnings are fatal in dune, and this can cause your code to not compile/be graded when you submit.

Submitting to Gradescope can be done using the exact same method used for project 0. Add your changes, commit them, push them, and then enter the submit keyword.

You can interactively test your code by doing `dune utop src` (assuming you have `utop`). Then you should be able to use any of the functions. All of your commands in `utop` need to end with two semicolons (i.e. `;;`), otherwise it will appear that your terminal is hanging.

Besides the provided public tests, you will also find the file **student.ml** on `test/student/`, where you'll be able to add OUnit tests of your own. More detailed information about writing tests can be found [here](https://www.youtube.com/watch?v=C36JnAcClOQ). Here are the timestamps for the topics covered in the video:

- Installing necessary software: [00:46](https://www.youtube.com/watch?v=C36JnAcClOQ&t=46s)
- How to build and test: [01:14](https://www.youtube.com/watch?v=C36JnAcClOQ&t=74s)
- List all available tests: [04:40](https://www.youtube.com/watch?v=C36JnAcClOQ&t=280s)
- Running a specific test: [05:05](https://www.youtube.com/watch?v=C36JnAcClOQ&t=305s)
- Testing inside of utop: [09:00](https://www.youtube.com/watch?v=C36JnAcClOQ&t=540s)
- Understanding test cases: [16:00](https://www.youtube.com/watch?v=C36JnAcClOQ&t=960s)
- Writing your own test cases: [19:20](https://www.youtube.com/watch?v=C36JnAcClOQ&t=1160s)

### Project Files

The following are the relevant files for your code:

- OCaml Files
    - **src/basics.ml**: You will **write your code here**, in this file. 
    - **src/basics.mli**: This file is used to describe the signatures of all the functions in the module.  *Do not modify this file*; Gradescope will use the original version.
    - **src/funs.ml**: This file includes implementation for some useful higher order functions. These are required for Part 4, but can be used throughout the project if you wish. *Do not modify this file* Gradescope will use the original version.
    - **src/funs.mli**: This file is used to describe the signatures of all the functions in the funs.ml.  *Do not modify this file*; Gradescope will use the original version.

### Important Notes about this Project

1. Some parts of this project are additive, meaning your solutions to earlier functions can be used to aid in writing later functions. Think about this in parts 3 and 4.
2. (IMPORTANT: This rule does not apply for Part 4 of this project). You can always add a helper function for any of the functions we ask you to implement, and the helper function can also be recursive. If you create a recursive helper function, the main function that calls the recursive helper does not have to be recursive/have the `rec` keyword in its function header. 
3. You may move around the function definitions. In OCaml, in order to use one function inside of another, you need to define the function before it is called. For example, if you think that a function from Part 2 can be used to help you implement a function in Part 1, you can move your implementation of the function from the Part 2 section to before the function in Part 1. As long as you still pass the tests and you haven't created a syntax error, you are fine.
4. Pay special notice to a function's type. Often times, you can lose sight of what you're trying to do if you don't remind yourself of the types of the arguments and the type of what you're trying to return.
5. You may rename arguments however you would like, but **do not modify function's name**. Doing so will cause you to fail the function's tests.

# Part 1: Non-Recursive Functions

Implement the following functions that do not require recursion. Accordingly, these functions are defined without the `rec` keyword, but **you MAY add the `rec` keyword to any of the following functions or write a recursive helper function**. Just remember that if you write a helper function, it must be defined in the file before it is called.

#### `rev_tup tup`

- **Type**: `'a * 'b * 'c -> 'c * 'b * 'a`
- **Description**: Returns a 3-tuple in the reverse order of `tup`.
- **Examples**:
   ```ocaml
   rev_tup (1, 2, 3) = (3, 2, 1)
   rev_tup (1, 1, 1) = (1, 1, 1)
   rev_tup ("a", 1, "c") = ("c", 1, "a")
   ```

#### `is_even x`

- **Type**: `int -> bool`
- **Description**: Returns whether or not `x` is even.
- **Examples**:
  ```ocaml
  is_even 1 = false
  is_even 4 = true
  is_even (-5) = false
  ```

#### `volume x y`

- **Type**: `int * int * int -> int * int * int -> int`
- **Description**: Takes in the Cartesian coordinates (3-dimensional) of two opposite corners of a rectangular prism and returns its volume. The sides of the rectangular prism are parallel to the axes.
- **Examples**:
  ```ocaml
  volume (1, 1, 1) (2, 2, 2) = 1
  volume (2, 2, 2) (1, 1, 1) = 1
  volume (0, 1, 2) (2, 3, 5) = 12
  volume (1, 1, 1) (1, 1, 1) = 0
  volume ((-1), (-1), (-1)) (1, 1, 1) = 8
  ```

# Part 2: Recursive Functions

Implement the following functions using recursion. You will lose points if this rule is not followed.
If you create a recursive helper function, the main function that calls the recursive helper does not have to be recursive/have the `rec` keyword in its function header.

#### `fibonacci n`

- **Type**: `int -> int`
- **Description**: Returns the `n`th term of the fibonacci sequence.
- **Assumptions**: `n` is non-negative, and we will **not** test your code for integer overflow cases.
- **Examples**:
  ```ocaml
  fibonacci 0 = 0
  fibonacci 1 = 1
  fibonacci 3 = 2
  fibonacci 6 = 8
  ```

#### `log x y`
- **Type**: `int -> int -> int`
- **Description**: Returns the log of `y` with base `x` rounded-down to an integer.
- **Assumptions**: You may assume the answer is non-negative, `x` >= 2, and `y` >= 1.
- **Examples**:
  ``` ocaml
  log 4 4 = 1
  log 4 16 = 2
  log 4 15 = 1
  log 4 64 = 3
  ```

#### `gcf x y`
- **Type**: `int -> int -> int`
- **Description**: Returns the greatest common factor of `x` and `y`.
- **Assumptions**: You may assume `x` >= `y` >= 0.
- **Examples**:
  ``` ocaml
  gcf 0 0 = 0
  gcf 3 0 = 3
  gcf 12 8 = 4
  gcf 24 6 = 6
  gcf 27 10 = 1
  gcf 13 13 = 13
  gcf 128 96 = 32
  ```

#### `maxFuncChain init funcs`
- **Type**: `'a -> ('a -> 'a) list -> 'a`
- **Description**: maxLambdaChain from Project 1 makes its return, OCaml style! This function takes in an initial value and a list of functions, and decides to either apply each function or not to maximize the final return value. For example, if we have a list of functions:
`[funcA; funcB; funcC]` and an initial value `x`, then we take the maximum value
of
   + `x`
   + `funcA(x)`
   + `funcB(funcA(x))`
   + `funcC(funcB(funcA(x)))`
   + `funcC(funcA(x))`
   + `funcB(x)`
   + `funcC(funcB(x))`
   + `funcC(x)`
- **Examples**:
  ```ocaml
  maxFuncChain 2 [(fun x -> x + 6)] = 8
  maxFuncChain 2 [(fun x -> x + 4); (fun x -> x * 4)] = 24
  maxFuncChain 4 [(fun x -> x - 2); (fun x -> x + 10)] = 14
  maxFuncChain 0 [(fun x -> x - 1); (fun x -> x * -500); (fun x -> x + 1)] = 501
  maxFuncChain "hello" [(fun x -> x ^ "1"); (fun x -> x ^ "2"); (fun x -> x ^ "3")] = "hello3"
  ```

# Part 3: Lists

#### `reverse lst`

- **Type**: `'a list -> 'a list`
- **Description**: Returns a list with the elements of `lst` but in reverse order.
- **Examples**:
  ```ocaml
  reverse [] = []
  reverse [1] = [1]
  reverse [1; 2; 3] = [3; 2; 1]
  reverse ["a"; "b"; "c"] = ["c"; "b"; "a"]
  ```

#### `zip lst1 lst2`

- **Type**: `('a * 'b) list -> ('c * 'd) list -> ('a * 'b * 'c * 'd) list`
- **Description**: Merge two tuple lists, `lst1` and `lst2`, and return the result as one tuple list. Tuples will only contain two elements. The final answer will have a length equivalent to the minimum of the input lengths.
- **Examples**:
  ```ocaml
  zip [(1, 2); (3, 4); (5, 6)] [(7, 8); (9, 10); (11, 12)] = [(1, 2, 7, 8); (3, 4, 9, 10); (5, 6, 11, 12)]
  zip [] [] = []
  zip [(1, 4)] [] = []
  zip [(1, 2); (3, 4)] [(7, 8)] = [(1, 2, 7, 8)]
  ```

#### `is_palindrome lst`

- **Type**: `'a list -> bool`
- **Description**: Returns true if `lst` is a palindrome and returns false otherwise. A palindrome is the same read forward and backward.
- **Important Note**: Use wildcards `_` to make sure all match cases are exhaustive.
- **Examples**:
  ```ocaml
  is_palindrome [] = true
  is_palindrome [1; 2; 3; 2; 1] = true
  is_palindrome ["A"; "b"; "b"; "A"] = true
  is_palindrome ["O"; "C"; "A"; "M"; "L"] = false
  ```

#### `square_primes lst`

- **Type**: `int list -> (int * int) list`
- **Description**: Returns a list of tuples `(a, b)` in which `a` is a prime number from `lst` and `b` is that prime number squared. If an element in `lst` is not a prime number, ignore it. You can
create a helper function to determine whether a number is prime or not. 
- **Examples**:
  ```ocaml
  square_primes [1; 2; 3; 4; 5] = [(2, 4); (3, 9); (5, 25)]
  square_primes [10; 11; 12; 13; 14] = [(11, 121); (13, 169)]
  square_primes [4; 6; 8] = []
  ```

#### `partition p lst`

- **Type**: `('a -> bool) -> 'a list -> 'a list * 'a list`
- **Description**: Returns a tuple of lists `(l1, l2)`, where `l1` is a list of all elements in `lst` that satisfy the predicate `p`, and `l2` is a list of all elements in `lst` that don’t satisfy the predicate `p`.
- **Examples**:
  ```ocaml
  partition (fun x -> x <= 2) [1; 2; 3; 4; 5] = ([1; 2], [3; 4; 5])
  partition (fun x -> x != 4) [10; 12; 14] = ([10; 12; 14], [])
  partition is_even [1; 2; 3; 4; 5] = ([2; 4], [1; 3; 5])
  ```

# Part 4: Higher Order Functions

Write the following functions using `map`, `fold`, or `fold_right` as defined in the file `funs.ml`. You **must** use `map`, `fold`, or `fold_right` to complete these functions, so none of the functions in Part 4 should be defined using the `rec` keyword. You also may not create recursive helper functions, but may use *any* function from parts 1-3. You will lose points if this rule is not followed. 

#### `is_present lst x`

- **Type**: `'a list -> 'a -> int list`
- **Description**: Returns a list of the same length as `lst` which has a `1` at each position in which the corresponding position in `lst` is equal to `x`, and a `0` otherwise.
- **Examples**:
  ```ocaml
  assert(is_present [1;2;3] 1 = [1;0;0]);;
  assert(is_present [1;1;0] 0 = [0;0;1]);;
  assert(is_present [2;0;2] 2 = [1;0;1]);;
  ```

#### `count_occ lst target`

- **Type**: `'a list -> 'a -> int`
- **Description**: Returns how many elements in `lst` are equal to `target`.
- **Examples**:
  ```ocaml
  assert(count_occ [] 1 = 0);;
  assert(count_occ [1] 1 = 1);;
  assert(count_occ [1; 2; 2; 1; 3] 1 = 2);;
  ```

#### `jumping_tuples lst1 lst2`

- **Type**: `('a * 'b) list -> ('c * 'a) list -> 'a list`
- **Description**: Given two lists of equal length of two element tuples, `lst1` and `lst2`, return a list based on the following conditions:
  + The first half of the list should be the first element of every odd indexed tuple in `lst1`, and the second element of every even indexed tuple in `lst2`, interwoven together (starting from index 0). 
  + The second half of the list should be the the first element of every even indexed tuple in `lst1`, and the second element of every odd indexed tuple in `lst2`, interwoven together (starting from index 0). 

For this function, consider 0 as even. Assume `lst1` and `lst2` are the same length. Consider using functions you have written above as helpers.

If you are having trouble understanding how this function works, we suggest to take a look at [this image](./jumping_tuples.png) and try to trace through the logic.
- **Examples**:
  ```ocaml
  jumping_tuples [(1, 2); (3, 4); (5, 6)] [(7, 8); (9, 10); (11, 12)] = [8; 3; 12; 1; 10; 5]
  jumping_tuples [(true,"a"); (false,"b")] [(100, false); (428, true)] = [false; false; true; true]
  jumping_tuples [("first", "second"); ("third", "fourth")] [("fifth", "sixth"); ("seventh", "eighth")] = ["sixth"; "third"; "first"; "eighth"]
  jumping_tuples [] [] = []
  ```

#### `addgenerator x`

- **Type**: `int -> (int -> int)`
- **Description**: Given an int, `x`, return a function that adds `x` to its parameter.
- **Examples**:
  ```ocaml
  assert((addgenerator 4) 3 = 7);;
  assert((addgenerator 1) 4 = 5);;
  assert((addgenerator 11) 11 = 22);;
  ```
#### `uniq lst`

- **Type**: `'a list -> 'a list`
- **Description**: Given a list, returns a list with all duplicate elements removed. *Order does not matter, in the output list.*
- **Examples**:
  ```ocaml
  assert(uniq [] = []);;
  assert(uniq [1] = [1]);;
  assert(uniq [1; 2; 2; 1; 3] = [2; 1; 3]);;
  ```

#### `ap fns args`

- **Type**: `('a -> 'b) list -> 'a list -> 'b list`
- **Description**: Applies each function in `fns` to each argument in `args` in order, collecting all results in a single list.
- **Examples**:
  ```ocaml
  assert(ap [] [1;2;3;4] = []);;
  assert(ap [succ] [] = []);;
  assert(ap [(fun x -> x^"?"); (fun x -> x^"!")] ["foo";"bar"] = ["foo?";"bar?";"foo!";"bar!"]);;
  assert(ap [pred;succ] [1;2] = [0;1;2;3]);;
  assert(ap [int_of_float;fun x -> (int_of_float x)*2] [1.0;2.0;3.0] = [1; 2; 3; 2; 4; 6]);;
  ```

(Here, `succ`, `pred`, and `int_of_float` are standard library functions. The `(^)` function is string concatenation.) 

## Academic Integrity

Please **carefully read** the academic honesty section of the course syllabus. **Any evidence** of impermissible cooperation on projects, use of disallowed materials or resources, or unauthorized use of computer accounts, **will be** submitted to the Student Honor Council, which could result in an XF for the course, or suspension or expulsion from the University. This includes posting this project to GitHub after the course is over. Be sure you understand what you are and what you are not permitted to do in regards to academic integrity when it comes to project assignments. These policies apply to all students, and the Student Honor Council does not consider lack of knowledge of the policies to be a defense for violating them. Full information is found in the course syllabus, which you should review before starting.
