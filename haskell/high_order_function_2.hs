
map' :: (a -> b) -> [a] -> [b]   
map' _ [] = []   
map' f (x:xs) = f x : map f xs

filter' :: (a -> Bool) -> [a] -> [a]   
filter' _ [] = []   
filter' p (x:xs)    
    | p x       = x : filter p xs   
    | otherwise = filter p xs

main = do
    print $ map' (+3) [1,5,3,1,6]
    print $ map' (++ "!") ["BIFF","BANG","POW"]   
    print $ map' (replicate 3) [3..6]  
    print $ map' (map (^2)) [[1,2],[3,4,5,6],[7,8]]  
    print $ map' fst [(1,2),(3,5),(6,3),(2,6),(2,5)]   
    print $ filter' (>3) [1,5,3,2,1,6,4,3,2,1]   
    print $ filter' (==3) [1,2,3,4,5]
    print $ filter' even [1..10]
