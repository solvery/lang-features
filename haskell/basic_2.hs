-- :: type

s :: String
s = "constant"

main = do
-- values
    putStrLn $ "haskell " ++ "lang"
    putStrLn $ "1+1 = " ++ show (1+1)
    putStrLn $ "7.0/3.0 = " ++ show (7.0/3.0)

    print $ True && False
    print $ True || False
    print $ not True

-- variable
    let v1 = "hello"
    putStrLn v1

    let v2 = 1
    let v3 = 2
    print v2 >> print v3

    let v4 =  True
    print v4 

    -- let e = undefined :: Int
    -- print e

    let f = "short"
    putStrLn f

-- constants
    putStrLn s

    let c2 = 500000000
    let c3 = 3e20 / c2

    print c2
    print $ sin c2

-- type parsing
    print (read "1.234" :: Double)
    print (read "123"   :: Int)
    print (read "0x1c8" :: Int)
    print (read "wat"   :: Int)

