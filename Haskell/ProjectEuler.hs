import Functions.Math

prob001 = sum $ multiplesOfFactors [1..999] [3, 5]

prob002 = sum $ filter (even) $ takeWhile (< 4000000) (fib 1 2)