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
(define (square z)
  (* z z)
)

(define (square_sum d e)
    (+ (square d) (square e))
)

(define (sum_square_larger a b c)
  (if (>= a c)
    (square_sum a (if (>= b c) b c))
    (square_sum c (if (>= a b) a b))
  )
)

(sum_square_larger 3 4 5)
(sum_square_larger 3 4 2)

;1.8
(x/y^2+2y)/3

(define (averageTwo a b)
  (/ (+ a b) 2)
)

(define (findCube x y)
  (define aprxX (- x .01))
  (if (<= aprxX (expt y 3)) ;(/ (+ (* 2 y) (/ x (expt y 2))) 3)
    y
    (findCube x (averageTwo y (/ x y)))
    )
)

(findCube 9 1)
(findCube 9 3)

;1.10

;(A 1 10) =
;(A 2 4) =
;(A 3 3)=

;1.11


;1.12
