(define rember 
	(lambda (x lat)
		(cond ((null? lat) (quote ()))
			  ((eq? x (car lat)) (cdr lat))
			  (else (cons (car lat) (rember a (cdr lat))))
		)
	)
)

(define firsts
	(lambda (lst)
		(cond ((null? lst) (quote ()))
			  (else (cons (car (car lst)) (firsts (cdr lst))))
		)
	)
)
