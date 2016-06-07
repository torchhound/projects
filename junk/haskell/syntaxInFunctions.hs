lucky :: (Integral a) => a -> String --pattern matching
lucky 7 = "Lucky number seven!"
lucky x = "Better luck next time..."

identityBoundFive :: (Integral a) => a -> String
identityBoundFive 1 = "One"
identityBoundFive 2 = "Two"
identityBoundFive 3 = "Three"
identityBoundFive 4 = "Four"
identityBoundFive 5 = "Five"
identityBoundFive x = "Out of bounds 1-5" --catchall must be at the end

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)

addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)
addVectors a b = (fst a + fst b, snd a + snd b)

addVectors' :: (Num a) => (a, a) -> (a, a) -> (a, a)
addVectors' (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

--triple tuple extraction functions
first :: (a, b, c) -> a
first (x, _, _) = x

second :: (a, b, c) -> b
second (_, y, _) = y

third :: (a, b, c) -> c
third (_, _, z) = z --underscores indicate a lack of caring about the input element at that position

head' :: [a] -> a
head' [] = error "Empty list"
head' (x:_) = x 

tell :: (Show a) => [a] -> String
tell [] = "Empty list"
tell (x:[]) = "Single element: " ++ show x
tell (x:y:[]) = "Two elements: " ++ show x ++ " and " ++ show y
tell (x:y:_) = "More than 2 elements"

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs

capital :: String -> String
capital "" = "Empty string"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]

--Guards
bmiBerate :: (RealFloat a) => a -> String
bmiBerate bmi
	| bmi <= 18.5 = "Underweight"
	| bmi <= 25.0 = "Normal"
	| bmi <= 30.0 = "Fat"
	| otherwise = "Ham planet"

bmiBerateOne :: (RealFloat a) => a -> a -> String
bmiBerateOne weight height
	| weight / height ^ 2 <= 18.5 = "Underweight"
	| weight / height ^ 2 <= 25.0 = "Normal"
	| weight / height ^ 2  <= 30.0 = "Fat"
	| otherwise = "Ham planet"

max' :: (Ord a) => a -> a -> a
max' a b
	| a > b = a
	| otherwise = b

compare' :: (Ord a) => a -> a -> Ordering
a `compare'` b
 | a > b = GT
 | a == b = EQ
 | otherwise = LT

--Where

bmiBerateTwo :: (RealFloat a) => a -> a -> String
bmiBerateTwo weight height
	| bmi <= 18.5 = "Underweight"
	| bmi <= 25.0 = "Normal"
	| bmi <= 30.0 = "Fat"
	| otherwise = "Ham planet"
	where bmi = weight / height ^ 2	

