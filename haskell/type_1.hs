
-- data
data Bool = False | True
-- data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun 
data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun deriving (Show, Eq, Ord, Enum)

tomorrow Sun = Mon
tomorrow d = succ d

yesterday Mon = Sun
yesterday d = pred d

-- type
type Name = String
type Author = String
type ISBN = String
type Price = Float
-- first Book, type constructor
-- second Book, data constructor
-- data Book = Book Name Author ISBN Price deriving (Show, Eq)
data Book = Book {
    name    :: Name,
    author  :: Author,
    isbn    :: ISBN,
    price   :: Price
}

main = do
    print Mon
    print [Mon .. Sun]
