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