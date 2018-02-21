#lang racket

(define add1
  (lambda (x)
    (+ x 1)))

(define sub1
  (lambda (x)
    (- x 1)))

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

(define firsts
  (lambda (lst)
    (cond
      ((null? lst) (quote ()))
      (else (cons (car (car lst)) (firsts (cdr lst)))))))

(firsts '((a list) (of lists) (which contain) (several elements)))
(firsts '((a b) (c d) (e f)))

(define insertList
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) old) (cons (cons (car lat) new) (cdr lat)))
      (else (cons (car lat) (insertList new old (cdr lat)))))))

(insertList 'e 'd '(a b c d f g d h))

(define insertR
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) old) (cons old (cons new (cdr lat))))
         (else (cons (car lat)
                     (insertR new old (cdr lat)))))))))

(insertR 'e 'd '(a b c d f g d h))

(define insertL
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) old) (cons new lat))
         (else (cons (car lat)
                     (insertL new old (cdr lat)))))))))

(insertL 'e 'd '(a b c d f g d h))

(define subst
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) old) (cons new (cdr lat)))
         (else (cons (car lat) (subst new old (cdr lat)))))))))

(subst 'e 'i '(h i l l))

(define subst2
  (lambda (new o1 o2 lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((or (eq? (car lat) o1) (eq? (car lat) o2))
          (cons new (cdr lat)))
         (else (cons (car lat) (subst2 new o1 o2 (cdr lat)))))))))

(subst2 'o 'e 'a '(c r e a k))
(subst2 'o 'e 'a '(c r a e k))

(define multirember
  (lambda (x lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) x) (multirember x (cdr lat)))
         (else (cons (car lat) (multirember x (cdr lat)))))))))

(multirember 'o '(c r o o k))

(define multiInsertR
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) old)
          (cons (car lat) (cons new (multiInsertR new old (cdr lat)))))
         (else (cons (car lat)
                     (multiInsertR new old (cdr lat)))))))))

(multiInsertR 'e 'o '(c r o o k))

(define multiInsertL
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) old)
          (cons new (cons old (multiInsertL new old (cdr lat)))))
         (else (cons (car lat)
                     (multiInsertL new old (cdr lat)))))))))

(multiInsertL 'e 'o '(c r o o k))

(define multiSubst
  (lambda (new old lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((eq? (car lat) old)
          (cons new (multiSubst new old (cdr lat))))
         (else (cons (car lat) (multiSubst new old (cdr lat)))))))))

(multiSubst 'e 'o '(c r o o k))
(quote (end ch3))

(define plus
  (lambda (x y)
    (cond
      ((zero? y) x)
      (else
       (add1 (plus x (sub1 y)))))))

(plus 14 12)

(define minus
  (lambda (x y)
    (cond
      ((zero? y) x)
      (else (sub1 (minus x (sub1 y)))))))

(minus 12 12)
(minus 24 12)

(define addTup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else
       (plus (car tup) (addTup (cdr tup)))))))

(addTup '(1 2 3 4 5 6))
(addTup '(59 63 77 88 92))

(define multiply
  (lambda (x y)
    (cond
      ((zero? y) 0)
      (else (plus x (multiply x (sub1 y)))))))

(multiply 5 3)
;(multiply 549 600)

(define tupPlus
  (lambda (tup1 tup2)
    (cond
      ((null? tup2) tup1)
      ((null? tup1) tup2)
      (else (cons (plus (car tup1) (car tup2))
                  (tupPlus (cdr tup1) (cdr tup2)))))))

(tupPlus '(3 6 9 11 4) '(8 5 2 0 7))
(tupPlus '(3 7 8 1) '(4 6))

(define greaterThan
  (lambda (x y)
    (cond
      ;((and (zero? x) (zero? y)) (quote (equal)))
      ((zero? x) #f)
      ((zero? y) #t)
      (else (greaterThan (sub1 x) (sub1 y))))))

(greaterThan 1 3)
(greaterThan 15 6)
;(greaterThan 1 1)

(define lessThan
  (lambda (x y)
    (cond
      ;((and (zero? x) (zero? y)) (quote (equal)))
      ((zero? y) #f)
      ((zero? x) #t)
      (else (lessThan (sub1 x) (sub1 y))))))

(lessThan 1 4)
(lessThan 6 4)
;(lessThan 1 1)

(define equals
  (lambda (x y)
    (cond
      ((greaterThan x y) #f)
      ((lessThan x y) #f)
      (else #t))))

(equals 1 1)
(equals 1 2)
(equals 2 1)

(define raise
  (lambda (x y)
    (cond
      ((zero? y) 1)
      (else (multiply x(raise x (sub1 y)))))))

(raise 1 1)
(raise 2 3)
(raise 5 3)

(define division
  (lambda (x y)
    (cond
      ((lessThan x y) 0)
      (else (add1 (division (minus x y) y))))))

(division 15 3)

(define length
  (lambda (lat)
    (cond
      ((null? lat) 0)
      (else (add1 (length (cdr lat)))))))

(length '(hotdogs with ketchup lettuce and tomato))

(define pick
  (lambda (lat x)
    (cond
      ((zero? (sub1 x)) (car lat))
      (else (pick (cdr lat) (sub1 x))))))

(pick '(spaghetti and meatballs) 2)

(define remPick
  (lambda (x lat)
    (cond
      ((zero? (sub1 x)) (cdr lat))
      (else (cons (car lat) (remPick (sub1 x) (cdr lat)))))))

(remPick 3 '(spaghetti with marinara sauce))

(define noNums
  (lambda (lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((number? (car lat)) (noNums (cdr lat)))
         (else
          (cons (car lat) (noNums (cdr lat)))))))))

(noNums '(1 sack 2 of 3 flour))

(define allNums
  (lambda (lat)
    (cond
      ((null? lat) (quote ()))
      (else
       (cond
         ((number? (car lat)) (cons (car lat) (allNums (cdr lat))))
         (else
          (allNums (cdr lat))))))))

(allNums '(1 sack 2 of 3 flour))

(define eqan?
  (lambda (x y)
    (cond
      ((and (number? x) (number? y)) (equals x y))
      ((or (number? x) (number? y) #f))
      (else (eq? x y)))))

(eqan? 1 1)
(eqan? 1 2)
(eqan? 'atom 'atom)
(eqan? 'atom 'tuple)

(define occur
  (lambda (x lat)
    (cond
      ((null? lat) 0)
      (else
       (cond
         ((eq? (car lat) x) (add1 (occur x (cdr lat))))
         (else (occur x (cdr lat))))))))

(occur 1 '(1 2 3 1 4 5 1 6 1))

(define one?
  (lambda (x)
    (eqan? x 1)))

(one? 1)
(one? 2)

(define remPickOne
  (lambda (x lat)
    (cond
      ((one? x) (cdr lat))
      (else (cons (car lat) (remPickOne (sub1 x) (cdr lat)))))))

(remPickOne 3 '(spaghetti with marinara sauce))
(quote (end ch4))

(define remberStar
  (lambda (