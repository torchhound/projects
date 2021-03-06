doubleThis x = x + x
doubleThat x = x * 2
quadThis x = doubleThis (doubleThat x)
tripleUs x y = x * 3 + y * 3
quadSmall x = if x > 100 then x else quadThis x
sling = "fade"
another = "this"
single = 'A'
someNums = [1,2,3,4,5]
otherNums = [6,7,8,9]
conCat x y = x ++ y
consCat x y = x:y
index x y = x !! y
hd x = head x --1st element
tl x = tail x --all except 1st element
nt x = init x --all except last element
lt x = last x --last element
llength x = length x
empty x = null x
--lstCheck x = if null x == True then length x else False
rvrs x = reverse x
tk x y = take x y --returns x elements from y list starting at index 0
drp x y = drop x y --returns y list with x elements missing starting from 0 index
max x = maximum x --largest element
min x = minimum x --smallest element
sm x = sum x --adds up the elements of a list
prd x = product x --multiplies the elements of list x
lm x y = x `elem` y --returns true or false based on whether x is in y list
lazyOne = [1..100] --lazy evaluation
lazyEven = [2,4..20]
lazyOdd = [1,3..20]
lazyLower = ['a'..'z']
lazyUpper = ['A'..'Z']
cyc x = cycle x --takes list x and cycles it into an infinite list
rpt x = repeat x --creates an infinite list of just element x
rep x y = replicate x y --returns a list of x length composed entirely of y elements
setOne = [x * 2 | x <- [1..10]]
filterOne = [x * 2 | x <- [1..10], x * 2 >= 12]
--fizzBuzz = [if x `mod` 3 = 0 && x `mod` 5 == 0 then "fizzbuzz" else if x `mod` 3 = 0 then "fizz" else if x `mod` 5 == 0 then "buzz" else x | x <- [1..100]]
filterTwo xs ys = [x * y | x <- xs, y <- ys]
crackSplat xs = [if x < 10 || x > 100 then "Crack!" else "Splat!" | x <- xs]
nouns = ["man", "bear", "fly"]
adjectives = ["dead", "alive", "screaming"]
hilarity = [adjective ++ " " ++ noun | adjective <- adjectives, noun <- nouns]
length' xs = sum [1 | _ <- xs]
removeLowercase str = [s | s <- str, s `elem` ['A'..'Z']]
tuplePerson = ("Sam", "Gamgee", 45)
pairOne = (9,11)
pairTwo = (20, 16)
foot x = fst x --fst accepts a pair and returns the first element
send x = snd x --snd accepts a pair and returns the second element
bigTupleOne = (1,2,3,4,5)
bigTupleTwo = (6,7,8,9,10)
zp x y = zip x y --zip takes 2 lists and turns them into one list with each element of the same index paired up
triangles = [ (a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]
rightTriangles = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2]
rightTriangles' = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a + b + c == 24]
