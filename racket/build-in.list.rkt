#lang racket

; cons 也被称为pair，包含两个值，car 获取第一个值，cdr 获取第二个值。
; car, cdr 特殊的切片

(cons 'x 'y)
'(10 . 20)
(define pair (cons 10 20))
(car pair)
(cdr pair)

(cons 1 (cons 2 3))
(cons 1 (cons 2 (cons 3 '())))
(cons 1 (cons 2 empty))
(list 1 2 3)
(define l1 '(1 2 3 4 5 6 7 8))
(car l1)
(cdr l1)
(car (cdr l1))
(cadr l1)
(cdr (cdr l1))
(cddr l1)
(caddr l1)
(cddddr l1)

; 在Racket里，pair 不是 list，但 list 是 pair
(pair? '(1 . 2))
(list? '(1 . 2))
(pair? '(1 2))
(list? '(1 2))

; partition 把列表按给定的条件分成满足条件的；不满足条件的。

; vector 是固定长度的数组
; hash

; symbol 
;  '(1 2 3) 等价于 (quote (1 2 3))，而其会被racket进一步翻译成 (list '1 '2 '3)
; symbol 是代码和数据之间转化的桥梁
