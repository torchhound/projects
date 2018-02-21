removeLowerCase :: [Char] -> [Char]
removeLowerCase str = [ c | c <- str, c `elem` ['A'..'Z']]
addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z
factorial :: Integer -> Integer --Integer has larger max and min values than Int
factorial n = product [1..n]
circumference :: Float -> Float
circumference r = 2 * pi * r
circumference' :: Double -> Double
circumference' r = 2 * pi * r
