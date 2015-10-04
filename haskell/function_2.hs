-- multi return values

vals :: () -> (Int, Int)
vals () = (3, 7)

main = do
    let (a, b) = vals ()
    print a
    print b

    let (_, c) = vals ()
    print c
