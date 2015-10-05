
-- data
data Bool = False | True
-- data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun 
data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun deriving (Show, Eq, Ord, Enum)

data Shape = Circle Float Float Float | Rectangle Float Float Float Float deriving (Show)

tomorrow Sun = Mon
tomorrow d = succ d

yesterday Mon = Sun
yesterday d = pred d

main = do
    print Mon
    print [Mon .. Sun]
