open Printf
let my_data = [ "a"; "beautiful"; "day" ]
let () = List.iter (fun s -> printf "%s\n" s) my_data;;

let message = "Hello"
let hello () = print_endline message;;
