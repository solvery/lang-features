; dosync

; reference
(def song (ref #{}))
(deref song)
@song

;(ref-set song #{"Dangerous"})
(dosync (ref-set song #{"Dangerous"}))

(def singer (ref #{}))
(dosync (ref-set song #{"Dangerous"})
             (ref-set singer #{"MJ"}) )

(dosync (ref-set song (conj @song "heal the world")))
(dosync (alter song conj "heal the world"))

; commute, alter
(def counter (ref 0))
(defn next-counter [] (dosync (commute counter inc)))
;(defn next-counter [] (dosync (alter counter inc)))
(dotimes [_ 50] (.start (Thread. #(println (next-counter)))))

;
(def validate-song
	(partial every? #(not (nil? %))))
(def song (ref #{} :validator validate-song))
(dosync (alter song conj #{"Dangerous"}))
; (dosync (alter song conj #{}))
