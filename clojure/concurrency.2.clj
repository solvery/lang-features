;; ensure
(def account1 (ref 100))
(def account2 (ref 100))
(defn deduct [account n other]
      (dosync
          (if (>= (+ (- @account n) @other) 0)
              (alter account - n))))
;;设定关卡
(def barrier (java.util.concurrent.CyclicBarrier. 6001))
;; 3000 thread
(dotimes [_ 3000] (.start (Thread. #(do (.await  barrier) (deduct account1 200 account2) (.await  barrier)))))
(dotimes [_ 3000] (.start (Thread. #(do (.await  barrier) (deduct account2 200 account1) (.await  barrier)))))
(.await barrier)
(.await barrier)
(println @account1)
(println @account2)

(def account1 (ref 100))
(def account2 (ref 100))
(defn deduct [account n other]
      (dosync (ensure account) (ensure other)
          (if (>= (+ (- @account n) @other) 0)
              (alter account - n))))
(dotimes [_ 3000] (.start (Thread. #(do (.await  barrier) (deduct account1 200 account2) (.await  barrier)))))
(dotimes [_ 3000] (.start (Thread. #(do (.await  barrier) (deduct account2 200 account1) (.await  barrier)))))
(.await barrier)
(.await barrier)
(println @account1)
(println @account2)


