-- pattern match

func :: (Integral a) => a -> String   
func 1 = "One!"   
--- func x = "Not between 1 and 5" 
func 2 = "Two!"   
func 3 = "Three!"   
func 4 = "Four!"   
func 5 = "Five!"   
func x = "Not between 1 and 5" 

func2 :: (Integral a) => a -> String
func2 dig
    | dig == 1 = "one"
    | dig == 2 = "two"
    | dig == 3 = "three"
    | otherwise = "tired."

func3 :: (Integral a) => a -> a -> String
func3 x y
    | dig == 1 = "one"
    | dig == 2 = "two"
    | dig == 3 = "three"
    | otherwise = "tired."
    where dig = x + y

main = do
    print $ func 1
    print $ func 3
    print $ func 7

    print $ func2 1
    print $ func2 3
    print $ func2 7

