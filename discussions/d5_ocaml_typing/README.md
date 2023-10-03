# Discussion 5 - Friday, September 29th

## Reminders

1. Quiz 2 today, first 20 minutes
2. Exam 1 next **Thursday, October 5th**
   1. Topic list: [@706](https://piazza.com/class/lkimk0rc39wfi/post/706)
3. Project 3 due **Friday, October 6th @ 11:59 PM**
4. Quiz makeup policy: [@238](https://piazza.com/class/lkimk0rc39wfi/post/238)
   1. **Tuesday** immediately following a quiz, **30% penalty**
   2. MUST submit documentation — see Piazza post for form link

## Topics List

- Functional programming paradigms
- OCaml basics + HOFs
- OCaml typing & pattern matching basics

## Exercises

> **NOTE:** Feel free to skip around, there are a lot of examples! 🙃

1. Give the type for each of the following OCaml expressions:

   ```ocaml
   [1a] fun a b -> b < a

   [1b] fun a b -> b + a > b - a

   [1c] fun a b c -> (int_of_string c) * (b + a)

   [1d] fun a b c -> (if c then a else a) * (b + a)

   [1e] fun a b c -> [ a + b; if c then a else a + b ]

   [1f] fun a b c -> if a b != a c then (a b) else (c < 2.0)

   [1g] fun a b c d -> if a && b < c then d + 1 else b
   ```

2. Write an OCaml expression for each of the following types:

   ```ocaml
   [2a] int * bool list

   [2b] (int * float) -> int -> float -> bool list

   [2c] float -> string -> int * bool

   [2d] (int -> bool) -> int -> bool list

   [2e] ('a -> 'b) -> 'a -> 'a * 'b list

   [2f] ('a -> 'b) -> ('b -> 'c) -> 'a -> 'c

   [2g] 'a -> 'b list -> 'a -> 'a * 'a
   ```

3. Give the type for the following OCaml `let` binding:

   ```ocaml
   let rec f p x y =
   match x, y with
      | ([], []) -> []
      | ((a,b)::t1, c::t2) -> (p a c, p b c)::(f p t1 t2)
      | (_, _) -> failwith "error";;
   ```

More examples can be found in [last semester's OCaml discussion](https://github.com/cmsc330-umd/spring23/tree/main/discussions/d3_ocaml).

## Resources & Additional Readings

- Encouraged (but optional) readings
  - [Spring 2023 OCaml Discussion](https://github.com/cmsc330-umd/spring23/tree/main/discussions/d3_ocaml)
  - [cs3110 - Expressions in OCaml](https://cs3110.github.io/textbook/chapters/basics/expressions.html)
- OCaml typing / expression generators
  - https://nmittu.github.io/330-problem-generator/type_of_expr.html
  - https://nmittu.github.io/330-problem-generator/expr_of_type.html

