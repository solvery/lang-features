
;; atom
(def mem (atom {}))
(deref mem)
(reset! mem {:a 1})
(swap! mem assoc :b 2)
(def c (atom 1))
(compare-and-set! c 2 3)
(compare-and-set! c 1 3)

(defn make-cache [] (atom {}))
(defn putm [cache key value] (swap! cache assoc key value))
(defn getm [cache key] (key @cache))
(def cache (make-cache))
(putm cache :a 1)
(getm cache :a)
(putm cache :b 2)
(getm cache :b)

;; 

;;
(ns atom-perf)
(import 'java.util.concurrent.atomic.AtomicInteger)
(import 'java.util.concurrent.CountDownLatch)

(def a (AtomicInteger. 0))
(def b (atom 0))

;;为了性能，给java加入type hint
(defn java-inc [#^AtomicInteger counter] (.incrementAndGet counter))
(defn countdown-latch [#^CountDownLatch latch] (.countDown latch))

;;单线程执行缓存次数
(def max_count 1000000)
;;线程数 
(def thread_count 100)

(defn benchmark [fun]
  (let [ latch (CountDownLatch. thread_count)  ;;关卡锁
         start (System/currentTimeMillis) ]     ;;启动时间
       (dotimes [_ thread_count] (.start (Thread. #(do (dotimes [_ max_count] (fun)) (countdown-latch latch))))) 
       (.await latch)
       (- (System/currentTimeMillis) start)))
         

(println "atom:" (benchmark #(swap! b inc)))
(println "AtomicInteger:" (benchmark #(java-inc a)))

(println (.get a))
(println @b)

