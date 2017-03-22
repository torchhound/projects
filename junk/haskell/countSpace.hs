import Data.Char as Char

countSpace :: String -> Int -> Int
countSpace "" 0 = 0
countSpace start count = case start of 
    "" -> count
    start 
        | Char.isSpace $ head start -> countSpace (tail start) (count + 1)
        | otherwise -> countSpace (tail start) count

main :: IO ()
main = do
    line <- getLine
    print $ countSpace line 0