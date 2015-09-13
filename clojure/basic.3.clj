
(loop [i 1]
  (if (<= i 5)
      (do (println "hello 1")
          (recur (+ i 1)))))

(dotimes [_ 5]
  (println "hello 2"))

(def x 1)
(def y 2)
(if (< x 0) (- x) x)

(when (< x y)
  (println "x is less ")
  (println "than y"))

(cond (> x 0) 1
  (= x 0) 0
  true -1)
