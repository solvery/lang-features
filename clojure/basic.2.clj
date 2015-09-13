
(+ 1 1) 

; local variable
(let [x 3 y 4]
   (+ x y))

(let [[x y] [3 4]]
   (+ x y))

(let [x 3 y (* x x)]
   (+ x y))

; global variable
(def x 3)

; remove variable
(ns-unmap *ns* 'x)

nil

(nil? 3)

'x
(quote x)
(symbol? 'x)
(= 'x 'x)
:foo

(or (not true) (and true false))
(min 1 2 3)
(max 1 2 3)

(quot 7 3)
(rem 7 3)
(/ 7 3)
(/ 7 (* 3 1.0))

; math
(Math/pow 2 32)
(Math/sqrt 2)

;
(String/format "%s: %d %.2f"
   (to-array ["Foo" 7 13.457]))
(.equals "foo" "bar")
(.compareTo "foo" "bar")
