-- Record Syntax

data Person = Person { firstName :: String   
                     , lastName :: String   
                     , age :: Int   
                     , height :: Float   
                     , phoneNumber :: String   
                     , flavor :: String   
                     } deriving (Show)

data Car = Car { company :: String 
                 , model :: String 
                 , year :: Int 
                 } deriving (Show)

main = do
    let guy = Person "Buddy" "Finklestein" 43 184.2 "526-2928" "Chocolate"   
    print guy
    print $ firstName guy
    print $ flavor guy

    print $ Car {company="Ford", model="Mustang", year=1967} 
