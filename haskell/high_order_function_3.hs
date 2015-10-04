
sum' :: (Num a) => [a] -> a   
sum' xs = foldl (\acc x -> acc + x) 0 xs

main = do
    print $ sum' [1,2,3,4]
