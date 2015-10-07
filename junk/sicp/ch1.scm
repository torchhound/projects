;1.1
;10 = 10
;(+ 5 3 4) = 12
;(- 9 1) = 8
;(/ 6 2) = 3
;(+ (* 2 4) (- 4 6)) = 6
;(define a 3) =
;(define b (+ a 1)) =
;(+ a b (* a b)) = 19
;(= a b) = false
;(if (and (> b a) (< b (* a b)))
; b
; a) = 4
;(cond ((= a 4) 6)
;  ((= b 4) (+ 6 7 a))
;  (else 25)) = 16
;(+ 2 (if (> b a) b a)) = 6
;(* (cond ((> a b) a)
;  ((< a b ) b)
; (else -1))
;(+ a 1)) = 16

;1.2
(/ (+ 5 4 (- 2(- 3)(+ 6 .8))) (* 3 (- 6 2) (- 2 7)))

;1.3
(define (larger a b)
    (if (> a b) a b)
)

(define (square z)
  (* z z)
)

(define (sum_square_larger a b c) (
  (define x (square (larger a b)))
  (define y (square (larger b c)))
  (if (= x y) (+ (square (larger a c)) y) (+ x y))
))

(sum_square_larger 3 4 5)

;1.8


;1.10


;1.12
