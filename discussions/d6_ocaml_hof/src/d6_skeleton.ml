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

(* TODO *)
let rec fold_tree f b t = failwith "unimplemented"

let rec map_tree f t = failwith "unimplemented"

let add1 tree = failwith "unimplemented"

let sum tree = failwith "unimplemented"