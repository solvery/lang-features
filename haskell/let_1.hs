
main = do
    print $ 4 * (let a = 9 in a + 1) + 2   
    print $ [let square x = x * x in (square 5, square 3, square 2)] 
    print $ (let a = 100; b = 200; c = 300 in a*b*c, let foo="Hey "; bar = "there!" in foo ++ bar) 
    print $ (let (a,b,c) = (1,2,3) in a+b+c) * 100

