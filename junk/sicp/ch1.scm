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
(define (sum_larger a b c) (
  (define x (expt (cond ((> a b) a) ((> a c) a)) 2))
  (define y (expt (if (or (> c a) (> c b)) c b) 2))
  (+ x y)
))

;1.8


;1.10


;1.12