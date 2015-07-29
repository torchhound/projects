import Data.Time

timer = do
			work = 25
			break = 5
			breakOccur = False
			start = getCurrentTime
			stopWork = start + 25
			stopBreak = start + 5
			
			if start == stopWork
				then 
					putStrLn "Time for a break!" 
					breakOccur = True
					timer
					if breakOccur == True
							then
								if start == stopBreak
									then
										putStrLn "Get back to work."
										breakOccur = False
										timer
								else timer
					else timer
			else timer

main = do
		timer 
	