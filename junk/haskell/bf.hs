import Data.Char

main = do
		bfArray = []
		bfArrayPtr = 0
		filePtr = 0
		file <- getLine
		input <- readFile file 
		interpreter = if filePtr < length input then
			if x in input == + then bfArray !! bfArrayPtr + 1
			if x in input == - then bfArray !! bfArrayPtr - 1
			if x in input == > then bfArrayPtr + 1 
			if x in input == < then if bfArrayPtr != 0 then bfArrayPtr - 1
			if x in input == . then print chr bfArray !! bfArrayPtr
			if x in input == , then bfArray !! bfArrayPtr <- ord getLine
			if x in input == [ then if bfArray !! bfArrayPtr == 0 && {-] exists in bfArray-} then bfArrayPtr {-to index of ]-} else {-skip-}
			if x in input == ] then if bfArray !! bfArrayPtr == 0 then {-skip-} else {-to index of [-}
			filePtr + 1
			interpreter
			else interpreter
		interpreter 