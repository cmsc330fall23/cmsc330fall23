# Discussion 6 - Friday, October 6th

## Reminders

1. Project 3 due **tonight, October 6th @ 11:59 PM**
1. Exam 1 makeup **Tuesday, October 10th**
   1. Signup form + logistics: [@812](https://piazza.com/class/lkimk0rc39wfi/post/812)

## Notes

- OCaml [`map`](https://github.com/cmsc330-umd/spring23/tree/main/discussions/d4_hof#part-1-map) and [`fold`](https://github.com/cmsc330-umd/spring23/tree/main/discussions/d4_hof#part-2-fold) review

## Exercise

Let's build a custom `tree` data type in OCaml! First, we will define the `tree` type:

```ocaml
type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree
```

This recursively defines a `tree` to either be a:

- `Leaf`
- `Node` with a left sub-`tree`, a value, and a right sub-`tree`

Let's generalize `map` and `fold` to work on our new `tree` structure:

### `fold_tree f init tree`

- **Type**: `('a -> 'b -> 'a -> 'a) -> 'a -> 'b tree -> 'a`
- **Description**: Given a function `f`, accumulator `init`, and `tree`, iterate over the given tree using `f` and return the iterated value of type `'a`.

  The function `f` will take in three parameters: the value of the accumulator returned by the left branch of the node, the value of the current node, and the value of the accumulator returned by the right branch of the node, and should then return the new accumulated value of type `'a`.

- **Examples**:

  ```ocaml
  let tree_a = Node(Node(Leaf, "Hello", Leaf), " World", Node(Leaf, "!", Leaf))
  let tree_b = Node(Node(Leaf, 5, Leaf), 6, Leaf)
  let tree_c = Node(Node(Leaf, 4, Leaf), 5, Node(Leaf, 2, Leaf))

  fold_tree (fun l s r -> l ^ s ^ r) "" tree_a = "Hello World!"
  fold_tree (fun l x r -> max (max l x) r) 0 tree_b = 6
  ```

### `map_tree f tree`

- **Type**: `('a -> 'b) -> 'a tree -> 'b tree`
- **Description**: Given a function `f`, map all the values of the nodes in the tree using `f`. Note that the mapped tree should still return the same tree shape with the corresponding mapped nodes.
- **Challenge**: Can we implement `map_tree` using `fold_tree`?
- **Examples**:

  ```ocaml
  map_tree string_of_int tree_b = Node(Node(Leaf, "5", Leaf), "6", Leaf)
  map_tree (fun x -> x + 1) tree_c = Node(Node(Leaf, 5, Leaf), 6, Node(Leaf, 3, Leaf))
  ```

### `add1 tree`

- **Type**: `int tree -> int tree`
- **Description**: Given an `int tree`, return a new `int tree` with the same values in the old tree incremented by one.
- **Examples**:

  ```ocaml
  add1 tree_b = Node(Node(Leaf, 6, Leaf), 7, Leaf)
  add1 tree_c = Node(Node(Leaf, 5, Leaf), 6, Node(Leaf, 3, Leaf))
  ```

### `sum tree`

- **Type**: `int tree -> int`
- **Description**: Given an `int tree`, return the sum of all elements within it.
- **Examples**:

  ```ocaml
  sum tree_b = 11
  sum tree_c = 11
  ```

More notes & examples can be found in [last semester's OCaml HOF discussion](https://github.com/cmsc330-umd/spring23/tree/main/discussions/d4_hof).

## Addendum

The idea of mapping and folding over non-list data structures is not novel. We want these higher-order functions to be _data structure independent_. While in this discussion we have implemented the `fold` and `map` functions for the `tree` data structure, they are already built into the language and OCaml does have other data structures it supports. For example, OCaml supports sets from the `Set` module and sets have `map` and `fold`.

## Resources & Additional Readings

- [Spring 2023 OCaml HOF discussion](https://github.com/cmsc330-umd/spring23/tree/main/discussions/d4_hof)
