# Solutions
### `if true then 42 else 1 - 1`
`Int 42`

### `if 1 then 42 else 0`
`InterpreterFailure "invalid if arguments"`

### `true - false / true`
`InterpreterFailure "invalid div arguments"`

### `false and (true or true)`
`Bool false`

### `false and true or true`
`Bool true`

### `(false and (true or false)`
`ParserFailure "match_token error"`

### `true || false`
`LexerFailure "lexer error"`

### `(4 * 3) - 1`
`LexerFailure "lexer error"`

### `3 - (2 / 0)`
`InterpreterFailure "div by 0"`

### `10 - (if true and false then 10 else 0)`
`Int 10`
