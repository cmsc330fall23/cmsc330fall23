# Eval Addendum

Here is some operational semantics that you might find helpful for the functions `reduce`, `laze` and `eager`:

### `reduce`

$\cfrac{A(x) = e}{A; x \Rightarrow e} \qquad \cfrac{A; e \Rightarrow e_1}{A;(Lx. e) \Rightarrow A;(Lx. e_1)} \qquad \cfrac{A;e_2 \Rightarrow e_3}{A;((Lx.\ e_1) \ e_2) \Rightarrow A, x:e_3;\ e_1} \qquad \cfrac{A;e_1 \Rightarrow e_3
\qquad A;e_2 \Rightarrow e_4}{A;(e_1 \ e_2) \Rightarrow A;(e_3 \ e_4)}$ 

- When evaluating a variable just return the value of the variable
- When evaluating a function you want to evaluate the body first and then re-evaluate
- If it is the application of an function and a variable, you want to extend the environment and then evaluate the body of the function with this newly extended environment. 
- In any other application case we want to evaluate the two arguments separately and then re-evaluate them together

### `laze`

$\cfrac{x:e_2:A; e_1 \Rightarrow e_3}{A;((Lx. e_1) \ e_2) \Rightarrow A;e_3} \qquad \cfrac{A;e_1 \Rightarrow e_3
\qquad A;e_2 \Rightarrow e_4}{A;(e_1 \ e_2) \Rightarrow A;(e_3 \ e_4)}$

- When evaluating the application of an argument to a function we want to evaluate the body of the function after mapping the parameter to the argument.
- In any other application case we want to evaluate the two arguments separately and then re-evaluate them together
- Note that we do not need to worry about functions that look like: `((a ((Lx.x) b)) (c ((Ly.y) d)))`

### `eager`

$\cfrac{A;e_2 \Rightarrow e_3 \qquad e_2 \neq e_3}{A;((Lx. e_1) \ e_2) \Rightarrow A;((Lx. e_1) \ e_3)} \qquad \cfrac{A;e_2 \Rightarrow e_3 \quad x:e_2:A;e_1 \Rightarrow e_4 \qquad e_2 == e_3}{A;((Lx. e_1) \ e_2) \Rightarrow e_4} \qquad \cfrac{A;e_1 \Rightarrow e_3 \qquad A;e_2 \Rightarrow e_4}{A;(e_1 \ e_2) \Rightarrow A;(e_3 \ e_4)}$

- When evaluating the application of an argument to a function we want to see if the argument is equal or unequal to the evaluated argument
    - In the case they are equal we can add a mapping from parameter to the argument and reevaluate the body of the function
    - In the case they are unequal we can evaluate the application once again this time using the evaluated argument instead
- In any other application case we want to evaluate the two arguments separately and then re-evaluate them together
- Note that we do not need to worry about functions that look like: `((a ((Lx.x) b)) (c ((Ly.y) d)))`