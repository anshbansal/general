module Functions.Math
(
collatz,
factorial,
fib,
isMultipleOfAny,
quicksort,
multiplesOfFactors
) where

collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz n
    | even n =  n:collatz (n `div` 2)
    | odd n  =  n:collatz (n*3 + 1)

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n
    | n > 0 = n * factorial(n - 1)
    | otherwise = error "Factorial of this argument not supported"

fib a b = fibs
	where fibs = a : b : zipWith (+) fibs (tail fibs)

quicksort :: (Ord a) => [a] -> [a]
quicksort []      = []
quicksort (x:xs)  = smaller ++ [x] ++ greater
    where smaller = quicksort (filter (<=x) xs)
          greater = quicksort (filter (>x) xs)

isMultipleOfAny :: (Integral a) => a -> [a] -> Bool
x `isMultipleOfAny` factors = any (\f -> x `rem` f == 0) factors

multiplesOfFactors :: (Integral a) => [a] -> [a] -> [a]
multiplesOfFactors numList factors = filter (`isMultipleOfAny` factors) numList