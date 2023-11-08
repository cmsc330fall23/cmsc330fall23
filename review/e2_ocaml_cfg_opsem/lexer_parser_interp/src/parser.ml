open Lexer
open Failures

(* Types *)
type expr =
| Int of int
| Bool of bool
| And of expr * expr
| Or of expr * expr
| Sub of expr * expr
| Div of expr * expr
| If of expr * expr * expr

let match_token (toks : token list) (tok : token) : token list =
  match toks with
  | [] -> raise (ParserFailure "match_token error")
  | h::t when h = tok -> t
  | h::_ -> raise (ParserFailure "match_token error")

let lookahead toks = match toks with
   h::t -> h
  | _ -> raise (ParserFailure "lookahead error")


let rec parser (toks : token list) : expr =
  let (t, exp) = parse_Expr toks in
  if t <> [Tok_EOF] then
    raise (ParserFailure "parser error")
  else
    exp

and parse_Expr toks = 
  match lookahead toks with
  | Tok_If -> 
    let toks = match_token toks Tok_If in
    let toks, a = parse_Expr toks in
    let toks = match_token toks Tok_Then in
    let toks, b = parse_Expr toks in
    let toks = match_token toks Tok_Else in
    let toks, c = parse_Expr toks in
    (toks, If(a, b, c))
  | _ -> parse_Or toks

and parse_Or toks = 
  let toks, a = parse_And toks in
  match lookahead toks with
  | Tok_Or -> 
    let toks = match_token toks Tok_Or in
    let toks, b = parse_Or toks in
    (toks, Or(a, b))
  | _ -> toks, a

and parse_And toks = 
  let toks, a = parse_Sub toks in
  match lookahead toks with
  | Tok_And -> 
    let toks = match_token toks Tok_And in
    let toks, b = parse_And toks in
    (toks, And(a, b))
  | _ -> toks, a

and parse_Sub toks = 
  let toks, a = parse_Div toks in
  match lookahead toks with
  | Tok_Sub -> 
    let toks = match_token toks Tok_Sub in
    let toks, b = parse_Sub toks in
    (toks, Sub(a, b))
  | _ -> toks, a

and parse_Div toks = 
  let toks, a = parse_Prim toks in
  match lookahead toks with
  | Tok_Div -> 
    let toks = match_token toks Tok_Div in
    let toks, b = parse_Div toks in
    (toks, Div(a, b))
  | _ -> toks, a

and parse_Prim toks = 
  match toks with
  | Tok_Int(x)::toks -> toks, Int(x)
  | Tok_Bool(x)::toks -> toks, Bool(x)
  | Tok_LParen::toks -> 
    let toks, e = parse_Expr toks in
    let toks = match_token toks Tok_RParen in
    toks, e
  | _ -> raise (ParserFailure "parser error")