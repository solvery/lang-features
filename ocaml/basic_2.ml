(* comment. *)
(* comment can be (* nested *).*)

print_int 3;;
print_string "\n";;
print_float 3.0;;
print_string "\n";;
print_string "good!";;
print_string "\n";;

print_int ((3 + 4 - 5) / 2 );;
print_string "\n";;


let a = 1;;
let my_ref = ref 0;;
my_ref := 100;;
print_int !my_ref;;
print_string "\n";;

let myvar= ref "hello";;

let average a b =
let sum = a +. b in sum /. 2.0;;
