import qualified Data.Text as T

wordcount :: String -> Int
wordcount "" = 0
wordcount start = let count = T.splitOn (T.pack " ") (T.pack start) in 
	length count

main :: IO () 
main = do
	line <- getLine
	print $ wordcount line