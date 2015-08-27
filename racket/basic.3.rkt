#lang racket

; variable
; define 全局，一个
(define x 1)
; (define x (+ x 1))

; let   局部，多个
(let ([a 3]
      [b 4])
  (sqr (+ a b)))

; let* 互相引用
(let* ([x 10]
       [y (* x x)])
  (list x y))

; let-value 一次绑定多个值
(let-values ([(x y) (quotient/remainder 10 3)])
            (list x y))

; let*-values 
(let*-values ([(pi r rr) (values 3.14159 10 (lambda (x) (* x x)))]
              [(perimeter area) (values (* 2 pi r) (* pi (rr r)))])
             (list area perimeter))

; letrec 函数的参数要延迟到 let 语句的 body 里才能获得
    (letrec ([is-even? (lambda (n)
                        (or (zero? n)
                         (is-odd? (sub1 n))))]
             [is-odd? (lambda (n)
                 (and (not (zero? n))
                  (is-even? (sub1 n))))])
     (is-even? 12)
    )

; 条件语句也是函数
(if (positive? -5) (error "doesn't get here") 2)
(if (member 2 (list 1 2 3 4)) 1 (error "doesn't get here"))
(define score 55)
;
(if (> score 90) "A"
 (if (> score 70) "B"
  (if (> score 60) "Pass"
   "Not Pass")))

(cond [(> score 90) "A"]
 [(> score 70) "B"]
 [(> score 60) "Pass"]
 [else "Not Pass"])

(cond
 [(member 2 '(1 2 3 4)) => (lambda (l) (map sqr l))])

(member 2 '(1 2 3 4))

(or (and (> score 90) "A")
 (and (> score 70) "B")
 (and (> score 60) "Pass")
 "Not Pass")

; 函数式编程语言没有循环，只有递归
; 无论是什么形式的循环，其实都可以通过递归来完成。
; for
(for ([i '(1 2 3)])
 (display i))

(define (for/recursive l f)
 (if (> (length l) 0) (let ([h (car l)]
                            [t (cdr l)])
                       (f h)
                       (for/recursive t f))
  (void)))
    (for/recursive '(1 2 3) display)

; for
(for/list ([i '(1 2 3 4)]
           [name '("goodbye" "farewell" "so long")])
 (format "~a: ~a" i name))
(for*/list ([i '(1 2 3 4)]
            [name '("goodbye" "farewell" "so long")])
 (format "~a: ~a" i name))
