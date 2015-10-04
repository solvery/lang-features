
main = do
    let l1 = [1,2,3,4]
    print l1
    let l2 = 5:l1
    print l2

    print $ l1 !! 1
    print $ head l1
    print $ tail l1
    print $ last l1
    print $ init l1
    print $ length l1
    print $ null l1
    print $ null []
    print $ null [[]]
    print $ reverse l1
    print $ take 3 l1
    print $ drop 3 l1
    print $ minimum l1
    print $ maximum l1
    print $ sum l1
    print $ product l1
    print $ 4 `elem` l1

    print $ [1..10]
    print $ [2,4..10]
    print $ take 10 [2,4..]
    print $ take 10 (cycle [1,2,3])
    print $ replicate 3 10

    -- list comprehension, predicate
    print $ [x*2 | x <- [1..10]]
    print $ [x*2 | x <- [1..10], x*2 >= 12]
    print $ [x | x <- [50..100], x `mod` 7 == 3]
    print $ [ x | x <- [10..20], x /= 13, x /= 15, x /= 19] 
    print $ [ if x < 10 then "BOOM!" else "BANG!" | x <- [7..13], odd x]  
    print $ [ x*y | x <- [2,5,10], y <- [8,10,11]]

    print $ ['a'..'z']
    print $ ['Y'..'Z']
    
    print $ [3,2,1] > [2,1,0] 
    print $ [3,2,1] == [2,1,0] 
