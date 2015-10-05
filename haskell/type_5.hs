
data Car a b c = Car { company :: a 
                       , model :: b 
                       , year :: c 
                        } deriving (Show)

tellCar :: Car a b c -> String 
tellCar (Car {company = c, model = m, year = y}) = "This " ++ c ++ " " ++ m ++ " was made in " ++ show y

main = do
    let stang = Car {company="Ford", model="Mustang", year=1967}
    print $ tellCar stang "This Ford Mustang was made in 1967"
