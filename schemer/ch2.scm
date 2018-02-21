(define atom? 
	(lambda (x)
	(and (not (pair? x)) (not (null? x)))
	)
)
	
(define lat?
	(lambda (l)
		(cond ((null? l) #t)
			  ((atom? (car l)) (lat? (cdr l)))
			  (else #f)
		)
	)
)

(define member?
	(lambda (x lat)
		(cond ((null? lat) #f)
			  (else (or (eq? x (car lat))
						(member? x (cdr lat))
					)
				)
		)
	)
)