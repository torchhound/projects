import Data.Char

interpreter = | filePtr < length input =
			| take x in input == + = bfArray !! bfArrayPtr + 1
			| take x in input == - = bfArray !! bfArrayPtr - 1
			| take x in input == > = bfArrayPtr + 1 
			| take x in input == < = | bfArrayPtr != 0 = bfArrayPtr - 1
			| take x in input == . = print chr bfArray !! bfArrayPtr
			| take x in input == , = bfArray !! bfArrayPtr <- ord getLine
			| take x in input == [ = | bfArray !! bfArrayPtr == 0 && {-] exists in bfArray-} = bfArrayPtr {-to index of ]-} else {-skip-}
			| take x in input == ] = | bfArray !! bfArrayPtr == 0 = {-skip-} else {-to index of [-}
			filePtr + 1
			interpreter
			| otherwise = interpreter
			
main = do
		bfArray = []
		bfArrayPtr = 0
		filePtr = 0
		file <- getLine
		input <- readFile file 
		interpreter 