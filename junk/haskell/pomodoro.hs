import Data.Time

timer = do
			let work = 25
				break = 5
				breakOccur = False
				start = getCurrentTime
				stopWork = start + 25
				stopBreak = start + 5
			if start == stopWork
				then 
					"Time for a break!" 
					let breakOccur = True
					do
						timer
					if breakOccur == True
							then
								if start == stopBreak
									then
										"Get back to work."
										let breakOccur = False
										do
											timer
								else 
									do
										timer
					else 
						do
							timer
			else 
				do
					timer \n

main = do
		timer \n
	