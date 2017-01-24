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
(quote (end ch1))

(define lat?
  (lambda (x)
    (cond
      ((null? x) #t)
      ((atom? (car x)) (lat? (cdr x)))
      (else #f))))

(lat? '(Bacon and tuna sandwiches))

(define member?
  (lambda (x lat)
    (cond
      ((null? lat) #f)
      (else (or (eq? (car lat) x)
                (member? x (cdr lat)))))))

(member? 'meat '(mashed potatoes and meat gravy))
(member? 'delicious '(rotten old shoes))
(quote (end ch2))

(define rember
  (lambda (x lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) x) (cdr lat))
      (else (cons (car lat) (rember x (cdr lat)))))))

(rember 'bacon '(bacon lettuce and tomato))
(rember 'and '(bacon lettuce and tomato))