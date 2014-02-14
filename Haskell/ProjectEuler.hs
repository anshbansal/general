import Functions.Math

prob001 a b = sum [x | x <- a, product ( map (x `rem`) b ) == 0]