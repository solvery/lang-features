
(defn add [x y] (+ x y))

; argument
; optional, variable, default, named
(defn add1 ([a] a) ([a b] (+ a b)))
(defn add2 [a & [b]]
  (if (nil? b) a (+ a b)))
(defn add3 [a & b]
	(+ a (if b (reduce + 0 b) 0)))
(defn add4 [a & b]
  (if (nil? b) a (+ a (apply + b))))
(defn add5
  ([a] (add a 0))
  ([a b] (+ a b)))

; named args
(defn logarithm [{x :number b :base}] (/ (Math/log x) (Math/log b)))
(logarithm {:base 2 :number 8})

; lambda 
(fn [x] (* x x))

;; fib
(defn fib [n] 
    (if (= n 0) 0
        (if (= n 1) 1
            (+ (fib (- n 1)) (fib (- n 2))))))

(defn lazy-seq-fibo 
    ([] 
        (concat [0 1] (lazy-seq-fibo 0 1))) 
    ([a b] 
        (let [n (+ a b)] 
            (lazy-seq 
                (cons n (lazy-seq-fibo b n))))))

; closure
(println (reduce + 
    (filter even? 
        (take-while (fn [n] (< n 4000000)) (lazy-seq-fibo)))))

; 使用 # 创建闭包
(println (reduce + 
    (filter even? 
        (take-while #(< % 4000000) (lazy-seq-fibo)))))
