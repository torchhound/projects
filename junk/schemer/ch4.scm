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
		(cond ((null? lat) 0)
			   (else (add1 (_length (cdr lat)))) ;adds 1 on each recursive step until the lat is null
		)
	)
)

(define pick
	(lambda (n lat)
		(cond ((zero? (sub1 n)) (car lat)) ;if subtracting 1 from n is zero then this is the atom you have picked and it is returned
				(else (pick (sub1 n)(cdr lat))) 
		)
	)
)

(define rempick
	(lambda (n lat)
		(cond ((zero? (sub1 n)) (cdr lat)) 
				(else (cons (car lat) (rempick (sub1 n)(cdr lat))))
		)
	)
)

(define non-nums
	(lambda (lat)
		(cond ((null? lat) (quote())) ;1st Commandment
				(else (cond ((number? (car lat)) (no-nums (cdr lat))) ;is the car of lat a number if so then recurse on the cdr of lat
							 (else (cons (car lat) (no-nums (cdr lat)))) ;car lat is not a number and hence must be cons'd at the end of recursion to return lat minus any numbers
						)
				)
		)
	)
)

(define all-nums
	(lambda (lat)
		(cond ((null? lat) (quote()))
				(else (cond ((number? (car lat)) (cons (car lat) (all-nums (cdr lat)))) ;moving the primary recursion to return a list of extracted numbers
							 (else (all-nums (cdr lat))) ;ignoring atoms and continuing to recurse
						)
				)
		)
	)
)

(define equan?
	(lambda (a1 a2)
		(cond ((and (number? a1)(number? a2)) (= a1 a2))
			  ((or (number? a1) (number? a2)) #f)
			  (else (eq? a1 a2))
		)
	)
)

(define occur?
	(lambda (lat a)
		(cond ((null? lat) 0)
			  (else (cond ((eq? a (car lat)) (add1 (occur? a (cdr lat))))
						   (else (occur? a (cdr lat)))
					)
				)
		)
	)
)

(define one? ;can be simplified to 1 line (define one? (lambda (n) (= n 1)))
	(lambda (n)
		(cond ((zero? n) #f)
			  ((= n 1) #t)
			  (else #f)
		)
	)
)

(define rempick2
	(lambda (n lat)
		(cond ((one? n) (cdr lat)) 
			  (else (cons (car lat) (rempick2 (sub1 n)(cdr lat))))
		)
	)
)
			