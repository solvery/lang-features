
{"t" 1 "f" 0}

(def ih (hash-map "t" 1 "f" 0))
(map? ih)
(count ih)
(get ih "t")
(find ih "t")
(get ih "m" -1)

(def ih2 (assoc ih "t" 2))
(contains? ih "t")
(def ih2 (dissoc ih "t"))

(def ih3 (merge ih ih2))
(require 'clojure.set)

(def ih4 (clojure.set/map-invert ih))
(def hkeys (map (fn [p] (first p)) ih))
(def hvals (map (fn [p] (second p)) ih))

