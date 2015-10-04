
func1 :: Int -> Int
func1 x = x + x

func2 :: Int -> Int -> Int
func2 x y = x*2 + y*2

func3 :: Int -> Int -> Int -
func3 x y = func2 x + func2 y

plus :: Int -> Int -> Int
plus = (+)

plusPlus :: Int -> Int -> Int -> Int
plusPlus a b c = a + b + c

main = do
    let res = func1 1
    putStrLn $ "func1 " ++ show res
    let res = func2 1 2
    putStrLn $ "func2 " ++ show res


    let res = plus 1 2
    putStrLn $ "1+2 = " ++ show res

    let res = plusPlus 1 2 3
    putStrLn $ "1+2+3 = " ++ show res
