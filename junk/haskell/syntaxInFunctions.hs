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
	| bmi <= skinny = "Underweight"
	| bmi <= normal = "Normal"
	| bmi <= fat = "Fat"
	| otherwise = "Ham planet"
	where bmi = weight / height ^ 2	
	      skinny = 18.5
	      normal = 25.0
              fat = 30.0 --(skinny, normal, fat) = (18.5, 25.0, 30.0)

initials :: String -> String-> String
initials first last = [f] ++ ". " ++ [l] ++ "."
	where (f:_) = first
	      (l:_) = last

calcBmi :: (RealFloat a) => [(a, a)] -> [a]
calcBmi xs = [bmi w h | (w, h) <- xs]
	where bmi weight height = weight / height ^ 2

--let

cylinder :: (RealFloat a) => a -> a -> a
cylinder r h =
	let sideArea = 2 * pi * r * h
	    topArea = pi * r ^ 2
	in sideArea + 2 * topArea

meaning = 4 * (let a = 9 in a + 1) + 2

localScopeFunc = [let square x = x * x in (square 5, square 3, square 2)]

inlineBind = (let a = 100; b = 200; c = 300 in a * b * c, let foo = "Hey "; bar = "there!" in foo ++ bar) --inline let uses semicolons

tupleBind = (let (a, b, c) = (1, 2, 3) in a + b + c) * 100

calcBmi' :: (RealFloat a) => [(a, a)] -> [a]
calcBmi' xs = [bmi | (w, h) <- xs, let bmi = w / h ^ 2, bmi >= 25.0]

--case expressions

headOne :: [a] -> a
headOne xs = case xs of [] -> error "Empty list!"
		        (x:_) -> x

describeList :: [a] -> String
describeList xs = "The list is " ++ case xs of [] -> "empty."
					       [x] -> "a singleton list."
					       xs -> "greater than 1 element."

describeList' :: [a] -> String
describeList' xs = "The list is " ++ what xs
	where what [] = "empty."
	      what [x] = "a singleton list."
	      what xs = "greater than 1 element."
