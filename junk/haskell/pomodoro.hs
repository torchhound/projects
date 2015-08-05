import Data.Time

timer = do
			work = 25
			break = 5
			breakOccur = False
			start = getCurrentTime
			stopWork = start + 25
			stopBreak = start + 5
			
			| start == stopWork
				= 
					putStrLn "Time for a break!" 
					breakOccur = True
					timer
					| breakOccur == True
							=
								| start == stopBreak
									=
										putStrLn "Get back to work."
										breakOccur = False
										timer
								| otherwise = timer
					| otherwise = timer
			| otherwise = timer

main = do
		timer 
	