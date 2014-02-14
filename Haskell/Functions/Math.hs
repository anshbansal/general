module Functions.Math
(
factorial,
quicksort
) where


factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n
    | n > 0 = n * factorial(n - 1)
    | otherwise = error "Factorial of this argument not supported"


quicksort :: (Ord a) => [a] -> [a]
quicksort []      = []
quicksort (x:xs)  = smaller ++ [x] ++ greater
    where smaller = quicksort (filter (<=x) xs)
          greater = quicksort (filter (>x) xs)


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