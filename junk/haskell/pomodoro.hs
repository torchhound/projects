import Data.Time

main = do
	work = 25
	break = 5
	breakOccur = False
	start = getCurrentTime
	stopWork = start + 25
	stopBreak = start + 5
	if start = stopWork
		then 
			"Time for a break!" 
			breakOccur = True 
			main
				if breakOccur = True
					then
						if start = stopBreak
							then
								"Get back to work."
								breakOccur = False
								main
				else main
	else main \n