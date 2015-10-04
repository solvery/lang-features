
sum' :: (Num a) => [a] -> a   
sum' xs = foldl (\acc x -> acc + x) 0 xs

sum'' :: (Num a) => [a] -> a   
sum'' = foldl (+) 0 -- 会返回一个取list作参数的函数, currying

elem' :: (Eq a) => a -> [a] -> Bool   
elem' y ys = foldl (\acc x -> if x == y then True else acc) False ys

map' :: (a -> b) -> [a] -> [b]   
map' f xs = foldr (\x acc -> f x : acc) [] xs

maximum' :: (Ord a) => [a] -> a   
maximum' = foldr1 (\x acc -> if x > acc then x else acc)   
 
reverse' :: [a] -> [a]   
reverse' = foldl (\acc x -> x : acc) []   
 
product' :: (Num a) => [a] -> a   
product' = foldr1 (*)   
 
filter' :: (a -> Bool) -> [a] -> [a]   
filter' p = foldr (\x acc -> if p x then x : acc else acc) []   
 
head' :: [a] -> a   
head' = foldr1 (\x _ -> x)   
 
last' :: [a] -> a   
last' = foldl1 (\_ x -> x)

main = do
    print $ sum' [1,2,3,4]
    print $ sum'' [1,2,3,4]
