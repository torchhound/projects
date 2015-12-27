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

(define rember*