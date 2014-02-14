import Functions.Math

emptyList = error "Empty list not supported"

--Prob 1
myLast [] = emptyList
myLast a  = a !! (length a)

--Prob 2
myButLast [] = emptyList
myButLast a  = a !! (length a - 1)