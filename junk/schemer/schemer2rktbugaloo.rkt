#lang racket

(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

(atom? (quote ()))
(atom? "atom")
(atom? 1492)
(car '(1 2 3))
(cdr '(1 2 3))
(cons 'peanut '(butter and jelly))
(cons '(banana and) '(peanut butter and jelly))
(cons 'p '(eanut))
(null? (quote()))
(eq? '1 '2)
(eq? '1 '1)
(eq? 'false 'false)
(eq? #t #t)
(eq? #f #f)
(eq? '3.14 '3.14)
(eq? '3.14 '3.1415)