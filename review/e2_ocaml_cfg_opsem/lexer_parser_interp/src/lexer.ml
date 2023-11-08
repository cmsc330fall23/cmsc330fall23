open Failures
type token =
| Tok_Int of int
| Tok_Bool of bool
| Tok_If
| Tok_Then
| Tok_Else
| Tok_Or
| Tok_And
| Tok_Sub
| Tok_Div
| Tok_LParen
| Tok_RParen
| Tok_EOF


(* 
  Expr -> If | Or
  If -> if Expr then Expr else Expr
  Or -> And or Or | And
  And -> Sub and And | Sub
  Sub -> Div - Sub | Div
  Div -> Prim / Div | Prim
  Prim -> <int> | true | false | ( Expr )
*)


let rec lexer (input : string) : token list =
  let length = String.length input in

  let rec tok pos =
    if pos >= length then
      [Tok_EOF]

    else if Str.string_match (Str.regexp "if") input pos then
      Tok_If::(tok (pos + 2))
    else if Str.string_match (Str.regexp "then") input pos then
      Tok_Then::(tok (pos + 4))
    else if Str.string_match (Str.regexp "else") input pos then
      Tok_Else::(tok (pos + 4))

    else if Str.string_match (Str.regexp "or") input pos then
      Tok_Or::(tok (pos + 2))
    else if Str.string_match (Str.regexp "and") input pos then
      Tok_And::(tok (pos + 3))

    else if Str.string_match (Str.regexp "true") input pos then
      (Tok_Bool true)::(tok (pos + 4))
    else if Str.string_match (Str.regexp "false") input pos then
      (Tok_Bool false)::(tok (pos + 5))

    else if Str.string_match (Str.regexp "(") input pos then
      Tok_LParen::(tok (pos + 1))
    else if Str.string_match (Str.regexp ")") input pos then
      Tok_RParen::(tok (pos + 1))
    else if Str.string_match (Str.regexp "-") input pos then
      Tok_Sub::(tok (pos + 1))
    else if Str.string_match (Str.regexp "/") input pos then
      Tok_Div::(tok (pos + 1))

    else if Str.string_match (Str.regexp "-?[0-9]+") input pos then
      let value = Str.matched_string input in
      Tok_Int(int_of_string value)::(tok (pos + String.length value))
    else if Str.string_match (Str.regexp " ") input pos then
      tok (pos + 1)
    else
      raise (LexerFailure "lexer error")

  in tok 0;;

