#lang racket

; number
1234
(+ 1000000000000000000000000000000000000000000000000000000000000 4321)
1.4141414141414142e+27
(/ 2 3)
(/ 2 3.0)
1+2i
(number? 1.4)
(number? (/ 9 10))
(exact->inexact 1/3)
(floor 1.9)
(ceiling 1.01)
(round 1.5)

; string
(string? "Hello world")
(string #\R #\a #\c #\k #\e #\t)
(make-string 10 #\c)
(string-length "Tyr Chen")
(string-ref "Apple" 3)
(substring "Less is more" 5 7)
(string-append "Hello" " " "world!")
(string->list "Eternal")
(list->string '(#\R #\o #\m #\e))

(string-join '["this" "is" "my" "best" "part"])
(string-join '("随身衣物" "充电器" "洗漱用品") "，"
               #:before-first "打包清单："
               #:before-last "和"
               #:after-last "等等。")
(string-split "  foo bar  baz \r\n\t")
(string-split "股票，开盘价，收盘价，最高价，最低价" "，")
(string-trim "  foo bar  baz \r\n\t")
(string-replace "股票，开盘价，收盘价，最高价，最低价" "，" "\n")
(string-replace "股票，开盘价，收盘价，最高价，最低价" "，" "\n" #:all? #f)


