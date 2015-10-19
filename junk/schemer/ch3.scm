(define rember 
	(lambda (x lat)
		(cond ((null? lat) ())
			  ((eq? x (car lat)) (cdr lat))
			  (rember lat)
		)
	)
)