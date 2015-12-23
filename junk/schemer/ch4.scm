(define add1
	(lambda (n)
		(+ n 1)
	)
)

(define sub1
	(lambda (n)
		(- n 1)
	)
)

(define plus
	(lambda (x y)
		(cond ((zero? y) x)
			  (else (add1 (+ x (sub1 y))))
		)
	)
)

(define minus
	(lambda (x y)
		(cond ((zero? y) x)
			  (else (sub1 (- x (sub1 y))))
		)
	)
)

(define addTup
	(lambda (tup)
		(cond ((null? tup) 0)
			  (else (plus (car tup) (addTup cdr tup)))
		)
	)
)

(define x
	(lambda (n m)
		(cond ((zero? m) 0) ;checks if m aka the counter is zero which closes recursion
				(else (plus n(x n(sub1 m)))) ;adds n to the natural recursion of n where m acts as a counter for the number off additions
		)
	)
)

(define tup+
	(lambda (tup1 tup2)
		(cond ((and (null? tup1)(null? tup2)) (quote ()))
			  ((null? tup1) tup2) ;simplify?
			  ((null? tup2) tup1)
			  (else (cons (plus (car tup1) (car tup2)) (tup+ (cdr tup1) (cdr tup2))))
		)
	)
)

(define _>
	(lambda (n m)
		(cond ((zero? n) #f)
		      ((zero? m) #t)
			  (else (> (sub1 m)(sub1 n))
		)
	)
)

(define _<
	(lambda (n m)
		(cond ((zero? n) #f)
		      ((zero? m) #t)
			  (else (< (sub1 m)(sub1 n))
		)
	)
)

(define _=
	(lambda (n m)
		(cond ((> n m) #f)
			  ((< n m) #f)
			  (else #t)
		)
	)
)

(define power
	(lambda (n m)
		(cond ((zero? m) 1) ;((zero? n) 0) unnecessary
			  (else (x n(power n(sub1 m)))) ;multiplication with m as a counter
		)
	)
)

(define division ;originally weirdEquality 
	(lambda (n m)
		(cond ((< n m) 0)
			  (else add1 (division (minus n m) m))
		)
	)
)

(define _length
	(lambda (lat)
		(cond ((