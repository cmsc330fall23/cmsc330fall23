(* tree structure *)
type 'a tree = 
  | Leaf 
  | Node of 'a tree * 'a * 'a tree

(* helpers *)
let rec map f xs = 
  match xs with
      [] -> []
    | h::t -> (f h)::(map f t)

let rec fold f a lst =
    match lst with
    []->a
    |h::t->fold f (f a h) t

let rec fold_right f lst a =
    match lst with
    []->a
    |h::t-> f h (fold_right f t a)

(* hofs *)
let rec fold_tree f b t =
  match t with
  | Leaf           -> b
  | Node (l, v, r) -> let res_l = fold_tree f b l in
      let res_r = fold_tree f b r in
      f res_l v res_r

let rec map_tree f t =
  match t with
  | Leaf           -> Leaf
  | Node (l, v, r) -> let new_l = map_tree f l in
      let new_r = map_tree f r in
      Node (new_l, f v, new_r)

(* fold_tree variant for map_tree *)
let rec map_tree f t = 
  fold_tree (fun l v r -> Node(l, f v, r)) Leaf t

let add1 tree = map_tree (fun x -> x + 1) tree

let sum tree = fold_tree (fun x l r -> x + l + r) 0 tree

(* tests *)
let tree_a = Node(Node(Leaf, "Hello", Leaf), " World", Node(Leaf, "!", Leaf))
let tree_b = Node(Node(Leaf, 5, Leaf), 6, Leaf)
let tree_c = Node(Node(Leaf, 4, Leaf), 5, Node(Leaf, 2, Leaf))

fold_tree (fun l s r -> l ^ s ^ r) "" tree_a = "Hello World!"
fold_tree (fun l x r -> max (max l x) r) 0 tree_b = 6

map_tree string_of_int tree_b = Node(Node(Leaf, "5", Leaf), "6", Leaf)
map_tree (fun x -> x + 1) tree_c = Node(Node(Leaf, 5, Leaf), 6, Node(Leaf, 3, Leaf))

add1 tree_b = Node(Node(Leaf, 6, Leaf), 7, Leaf)
add1 tree_c = Node(Node(Leaf, 5, Leaf), 6, Node(Leaf, 3, Leaf))

sum tree_b = 11
sum tree_c = 11
