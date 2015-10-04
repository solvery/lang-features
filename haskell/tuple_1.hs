
main = do
    print $ (1,2)
    print $ [(1,2), (3,4), (5,6)]
    --- print $ [(1,2), (3,4), (5,6,7)]

    print $ fst (1,2)
    print $ snd (1,2)

    print $ zip [1,2,3,4,5] [5,5,5,5,5]
    print $ zip [1 .. 5] ["one", "two", "three", "four", "five"]  
    print $ zip [5,3,2,6,2,7,2,5,4,6,6] ["im","a","turtle"]
    print $ zip [1..] ["apple", "orange", "cherry", "mango"]
