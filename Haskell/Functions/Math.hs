module Functions.Math
(
factorial,
isMultipleOfAny,
quicksort,
sumOfMultiples
) where


factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n
    | n > 0 = n * factorial(n - 1)
    | otherwise = error "Factorial of this argument not supported"


isMultipleOfAny :: (Integral a) => a -> [a] -> Bool
x `isMultipleOfAny` factors = any (\f -> x `rem` f == 0) factors


quicksort :: (Ord a) => [a] -> [a]
quicksort []      = []
quicksort (x:xs)  = smaller ++ [x] ++ greater
    where smaller = quicksort (filter (<=x) xs)
          greater = quicksort (filter (>x) xs)


sumOfMultiples :: (Integral a) => [a] -> [a] -> a
sumOfMultiples numList factors = sum $ filter (`isMultipleOfAny` factors) numList


lastButOne :: [a] -> Maybe a
lastButOne [a, _] = Just a
lastButOne (_:xs) = lastButOne xs
lastButOne _ 	  = Nothing


isOdd :: (Integral a) => a -> Bool
isOdd a = mod a 2 == 1


collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz n
    | even n =  n:collatz (n `div` 2)
    | odd n  =  n:collatz (n*3 + 1)