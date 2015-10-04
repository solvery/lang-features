

main = do
    print $ map (\x -> x+3) [1,6,3,2]
    print $ zipWith (\a b -> (a * 30 + 3) / b) [5,4,3,2,1] [1,2,3,4,5]
    print $ map (\(a,b) -> a + b) [(1,2),(3,5),(6,3),(2,6),(2,5)]
    

