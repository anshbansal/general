module Functions 
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
quicksort []     = []
quicksort (x:xs) = smaller ++ [x] ++ greater
    where smaller = quicksort (filter (<=x) xs)
          greater = quicksort (filter (>x) xs)


lastButOne :: [a] -> a
lastButOne [a, b] = a
lastButOne (_:xs) = lastButOne xs
lastButOne a = error "Not Supported"

