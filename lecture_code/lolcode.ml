open Str
type token =
| Tok_Int of int
| Tok_Var of string
| Tok_SUM
| Tok_OF
| Tok_AN
| Tok_I
| Tok_HAS
| Tok_A
| Tok_ITZ
| Tok_nl
| Tok_PRODUKT
| Tok_WIN
| Tok_FAIL
| Tok_O
| Tok_RLY
| Tok_qm
| Tok_YA
| Tok_NO
| Tok_WAI
| Tok_OIC

let string_of_token tok = match tok with
| Tok_Int(x) -> string_of_int x
| Tok_Var(x) -> x
| Tok_SUM -> "SUM"
| Tok_OF -> "OF"
| Tok_AN -> "AN"
| Tok_I -> "I"
| Tok_HAS -> "HAS"
| Tok_A -> "A"
| Tok_ITZ -> "ITZ"
| Tok_nl -> "\n"
| Tok_PRODUKT -> "PRODUKT"
| Tok_WIN -> "WIN"
| Tok_FAIL -> "FAIL"
| Tok_O -> "O"
| Tok_RLY -> "RLY"
| Tok_qm -> "?"
| Tok_YA -> "YA"
| Tok_NO -> "NO"
| Tok_WAI -> "WAI"
| Tok_OIC -> "OIC"


let rec string_of_list conv lst = 
match lst with
| [] -> ""
| h::[] -> conv h
| h::t -> (conv h) ^ " " ^ (string_of_list conv t)

(* Given source code returns a token list. *)
let rec lexer (input) =
  let length = String.length input in

  let rec tok pos =
    if pos >= length then
      []

    else if Str.string_match (Str.regexp "SUM") input pos then
      Tok_SUM::(tok (pos + 3))
    else if Str.string_match (Str.regexp "PRODUKT") input pos then
      Tok_PRODUKT::(tok (pos + 7))
    else if Str.string_match (Str.regexp "OF") input pos then
      Tok_OF::(tok (pos + 2))
    else if Str.string_match (Str.regexp "AN") input pos then
      Tok_AN::(tok (pos + 2))
    else if Str.string_match (Str.regexp "HAS") input pos then
      Tok_HAS::(tok (pos + 3))
    else if Str.string_match (Str.regexp "ITZ") input pos then
      Tok_ITZ::(tok (pos + 3))
    else if Str.string_match (Str.regexp "RLY") input pos then
      Tok_RLY::(tok (pos + 3))
    else if Str.string_match (Str.regexp "YA") input pos then
      Tok_YA::(tok (pos + 2))
    else if Str.string_match (Str.regexp "NO") input pos then
      Tok_NO::(tok (pos + 2))
    else if Str.string_match (Str.regexp "WAI") input pos then
      Tok_WAI::(tok (pos + 3))
    else if Str.string_match (Str.regexp "OIC") input pos then
      Tok_OIC::(tok (pos + 3))
    else if Str.string_match (Str.regexp "WIN") input pos then
      Tok_WIN::(tok (pos + 3))
    else if Str.string_match (Str.regexp "FAIL") input pos then
      Tok_FAIL::(tok (pos + 4))
    else if Str.string_match (Str.regexp "A") input pos then
      Tok_A::(tok (pos + 1))
    else if Str.string_match (Str.regexp "I") input pos then
      Tok_I::(tok (pos + 1))
    else if Str.string_match (Str.regexp "O") input pos then
      Tok_O::(tok (pos + 1))
    else if Str.string_match (Str.regexp "\n") input pos then
      Tok_nl::(tok (pos + 1))
    else if Str.string_match (Str.regexp "?") input pos then
      Tok_qm::(tok (pos + 1))

    else if Str.string_match (Str.regexp "-?[0-9]+") input pos then
      let value = Str.matched_string input in
      Tok_Int(int_of_string value)::(tok (pos + String.length value))

    else if Str.string_match (Str.regexp "[a-z]+") input pos then
      let value = Str.matched_string input in
      Tok_Var(value)::(tok (pos + String.length value))

    else if Str.string_match (Str.regexp " ") input pos then
      tok (pos + 1)
    else
      failwith ("lexing error:" ^ (String.sub input pos (1)))

  in tok 0



(* GRAMMAR 
E ->  x
     |n, n is a NUMBR
     |t, t is a TROOF
     |I HAS A x ITZ E\nE
     |SUM OF E AN E
     |PRODUKT OF E AN E
     |O E?\nYA RLY\nE\nNO WAI\nE\nOIC

3
WIN
I HAS A var ITZ4
  var
SUM OF 3 AN 4
PRODUKT OF 3 AN 4
O WIN?
  YA RLY
    FAIL
  NO WAI
    WIN
  OIC
*)

(* Types *)
type expr =
| Int of int
| Var of string
| HAS of string * expr * expr
| SUM of expr * expr
| PRODUKT of expr * expr
| TROOF of bool
| RLY of expr * expr * expr

(* Parses a token list. *)
let parser (toks) =
  let rec parse toks = 
    match toks with
     Tok_Int(x)::t -> Int(x),t
    |Tok_WIN::t -> TROOF(true),t
    |Tok_FAIL::t -> TROOF(false),t
    |Tok_Var(x)::t -> Var(x),t
    |Tok_I::Tok_HAS::Tok_A::Tok_Var(var)::Tok_ITZ::t -> 
      let e1,toks' = parse t in
      (match toks' with
         Tok_nl::t -> let e2,toks'' = parse t in 
          HAS(var,e1,e2),toks''
        |x::_ -> (raise (Failure ("Expected nl; Got " ^ string_of_token x)))
        |_ -> (raise (Failure ("Expected nl; Ended prematurely"))))
    |Tok_SUM::Tok_OF::t -> 
      let e1,toks' = parse t in
      (match toks' with
         Tok_AN::t -> let e2,toks'' = parse t in
          SUM(e1,e2),toks''
        |x::_ -> (raise (Failure ("Expected AN; Got " ^ string_of_token x)))
        |_ -> (raise (Failure ("Expected AN; Ended prematurely"))))
    |Tok_PRODUKT::Tok_OF::t -> let e1,toks' = parse t in
                               (match toks' with
                                 Tok_AN::t -> let e2,toks'' = parse t in
                                              PRODUKT(e1,e2),toks''
                                |_ -> raise (Failure "Missing AN"))
    |Tok_O::t -> 
      let e1,toks' = parse t in
        (match toks' with 
           Tok_qm::Tok_nl::Tok_YA::Tok_RLY::Tok_nl::t -> 
             let e2,toks'' = parse t in
             (match toks'' with
                Tok_nl::Tok_NO::Tok_WAI::Tok_nl::t -> 
                  let e3,toks''' = parse t in
                  (match toks''' with 
                     Tok_nl::Tok_OIC::t -> RLY(e1,e2,e3),t
                    |_ -> raise (Failure "Missing OIC"))
               |_ -> raise (Failure "Missing NO WAI branch"))
          |_ -> raise (Failure "Malformed O expression") 
                )
    |x -> raise (Failure ("Malformed sentence: " ^ string_of_list (string_of_token) x))
  in 
  let (exp,t) = parse toks in
  if t <> [] then
    raise (Failure "Left over tokens")
  else
    exp
(*
type expr =
| Int of int
| Var of string
| HAS of string * expr * expr
| SUM of expr * expr
| PRODUKT of expr * expr
| TROOF of bool
*)
let rec lookup env var = match env with
  [] -> raise (Failure "Unbound var")
  |(x,value)::t -> if x = var then value else lookup t var

type value = NUMBR of int|BOOL of bool

let interp ast = 
  let rec lolcode env ast = match ast with
     Int(x) -> NUMBR(x)
    |TROOF(x) -> BOOL(x)
    |Var(x) -> lookup env x
    |HAS(var,e1,e2) -> let v1 = lolcode env e1 in
                       let extenv = (var,v1)::env in
                       let v2 = lolcode extenv e2 in
                       v2
    |SUM(e1,e2) -> let v1 = lolcode env e1 in 
                   let v2 = lolcode env e2 in
                   (match v1,v2 with
                     NUMBR(n1),NUMBR(n2) -> NUMBR(n1+n2)
                    |_ -> raise (Failure "Type error"))
    |PRODUKT(e1,e2) -> let v1 = lolcode env e1 in
                       let v2 = lolcode env e2 in 
                       (match v1,v2 with
                         NUMBR(n1),NUMBR(n2) -> NUMBR(n1*n2)
                        |_ -> raise (Failure "Type error"))
    |RLY(e1,e2,e3) -> let guard = lolcode env e1 in
                      (match guard with
                         BOOL(x) when x -> lolcode env e2
                        |BOOL(x) -> lolcode env e3
                        |_ -> raise (Failure "Type error"))
  in lolcode [] ast
