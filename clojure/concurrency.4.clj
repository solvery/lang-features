
(def counter (agent 0))
(deref counter)
(send counter inc)
(send-off counter inc)



