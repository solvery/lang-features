#lang racket

(+ 1 1)
(+ 2 4 6)
(* 2 (+ 3 4))
(expt 2 3)
(/ 35 7) 
(/ 4 6)
(exact->inexact 2/3)

(* 1+2i 3+4i)

(not #t)
(and -1 #f)
(and -1 2)
(or -1 #f)
(or #f #f)
(xor #f 10)
(xor 10 20)
(> 1 2)
(< 1 2)
(= 10 20)

(string-append "你好" "，" "世界！")
(format "~a，~a！" "你好" "世界")
(printf "~a，~a！" "你好" "世界")

(number->string 42)
(string->number "42")
(string->number "hello world")
(string-length "hello world!")
(string-length "你好，世界！")
(string? "你好")
(number? "1")
(number? 1+2i)

