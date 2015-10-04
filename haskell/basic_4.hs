
main = do
    let i = 2
    putStr $ "write " ++ show i ++ " as "
    case i of
        1 -> putStrLn "one"
        2 -> putStrLn "two"
        3 -> putStrLn "three"

    let week = 3
    putStrLn $
        case week of
            6 -> "it's the weekend"
            7 -> "it's the weekend"
            _ -> "it's a weekday"

    let hour = 15
    case hour of
        _
            | hour < 12 -> putStrLn "it's before noon"
            | otherwise -> putStrLn "it's after noon"
