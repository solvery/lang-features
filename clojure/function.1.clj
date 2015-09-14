
(defn add [x y] (+ x y))

; argument
; optional, variable, default, named
(defn add1 ([a] a) ([a b] (+ a b)))
(defn add2 [a & [b]]
  (if (nil? b) a (+ a b)))

( defn add3 [a & b]
	(+ a (if b (reduce + 0 b) 0)))

; named args
(defn logarithm [{x :number b :base}] (/ (Math/log x) (Math/log b)))
(logarithm {:base 2 :number 8})

; lambda 
(fn [x] (* x x))
