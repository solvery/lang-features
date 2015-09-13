
(try (throw (Exception. "failure"))
  (catch Exception e
    (printf "error: %s\n"
      (.getMessage e))))

(try (/ 1 0) (catch ArithmeticException _ (do (println "division by zero") nil)))

(try (throw (Exception. "failure"))
     (finally (println "clean up")))

;(throw (Exception. "failed"))

