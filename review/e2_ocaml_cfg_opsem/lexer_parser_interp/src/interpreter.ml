open Parser
open Lexer
open Failures

type value =
| Int of int
| Bool of bool

let rec eval (ast: expr): value =
  match ast with
  | Int x -> Int x
  | Bool x -> Bool x
  | Div (x, y) -> (
    match (eval x, eval y) with
    | (Int x, Int y) -> 
      if y == 0 then raise (InterpreterFailure "div by 0") 
      else Int (x / y)
    | _ -> raise (InterpreterFailure "invalid div arguments"))
  | Sub (x, y) -> (
    match (eval x, eval y) with
    | (Int x, Int y) -> Int (x - y)
    | _ -> raise (InterpreterFailure "invalid sub arguments"))
  | And (x, y) -> (
    match (eval x, eval y) with
    | (Bool x, Bool y) -> Bool (x && y)
    | _ -> raise (InterpreterFailure "invalid and arguments"))
  | Or (x, y) -> (
    match (eval x, eval y) with
    | (Bool x, Bool y) -> Bool (x || y)
    | _ -> raise (InterpreterFailure "invalid or arguments"))
  | If (guard, t, f) -> (
    match (eval guard, eval t, eval f) with
    | (Bool guard, t, f) -> if guard then t else f
    | _ -> raise (InterpreterFailure "invalid if arguments"))
