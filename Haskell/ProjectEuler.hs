module ProjectEuler
(
) where

import Functions

prob001 :: (Integral a) => [a] -> [a] -> a
prob001 a b = sum [x | x <- a, product ( map (x `rem`) b ) == 0]

