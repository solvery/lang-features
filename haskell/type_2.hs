-- type 类型别名

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
} deriving (Show, Eq)

main = do
    print ""
