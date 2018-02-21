#lang racket

(define (kwic-read filename)
	(with-input-from-filename filename
		(lambda ()
			(for/list ([line (in-lines)])
line))))

(define (kwic-split lines)
	(map string-split lines))

(define (circular-shift words)
	(append (rest words) (list (first words))))

(define (all-circular-shifts words)
	(for/fold ([all-shifts (list words)])
			([i (in-range 1 (length words))])
		(cons (circular-shift (first all-shifts))
			all-shifts)))

(define (alphabetize all-shifts)
	(sort all-shifts shift<?))

(define (shift<? shift1 shift2)
	(match* (shift1 shift2)
		[('() _)
			#t]
		[(_ ' ())
			#f]
		[((cons s1 shift1-rest) (cons s2 shift2-rest))
			(or (string<? s1 s2)
				(and (string=? s1 s2)
					(shift<? shift1-rest shift2-rest)))]))

(define (kwic-display all-sorted-shifts)
	(define (display-words words)
		(display (first words))
		(for ([word (in-list (cdr words))])
			(display " ")
			(display word))
		(newline))
	(for-each display-words all-sorted-shifts))
