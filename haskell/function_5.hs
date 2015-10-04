-- pattern match

sayMe :: (Integral a) => a -> String   
sayMe 1 = "One!"   
--- sayMe x = "Not between 1 and 5" 
sayMe 2 = "Two!"   
sayMe 3 = "Three!"   
sayMe 4 = "Four!"   
sayMe 5 = "Five!"   
sayMe x = "Not between 1 and 5" 

sayMe2 :: (Integral a) => a -> String
sayMe2 dig
    | dig == 1 = "one"
    | dig == 2 = "two"
    | dig == 3 = "three"
    | otherwise = "tired."

main = do
    print $ sayMe 1
    print $ sayMe 3
    print $ sayMe 7

    print $ sayMe2 1
    print $ sayMe2 3
    print $ sayMe2 7

