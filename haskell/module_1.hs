
import Data.Function (on)
import Data.List
import Data.Char

main = do
    print $ all isAlphaNum "bobby283"   
    print $ all isAlphaNum "eddy the fish!"   
    print $ words "hey guys its me"   
    print $ groupBy ((==) `on` isSpace) "hey guys its me"   
    print $ generalCategory ' '   
    print $ generalCategory 'A'   
    print $ generalCategory 'a'   
    print $ generalCategory '.'   
    print $ generalCategory '9'   
    print $ map generalCategory " \t\nA9?|"   
    print $ map digitToInt "34538"   
    print $ map digitToInt "FF85AB"   
    print $ intToDigit 15   
    print $ intToDigit 5   
    print $ ord 'a'   
    print $ chr 97   
    print $ map ord "abcdefgh"   
