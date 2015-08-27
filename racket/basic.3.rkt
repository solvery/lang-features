#lang racket

(require 2htdp/image)
(define flag (rectangle 100 61.8 "solid" "red"))
flag

(define big-star (star 15 "solid" "yellow"))
big-star
(overlay big-star flag)

(overlay/xy (rectangle 20 20 "solid" "red")
    10 10
    (rectangle 20 20 "solid" "black"))
; Racket约定使用 / 符号的函数代表其属于同一族，即 overlay/xy 是 overlay 的变体。

