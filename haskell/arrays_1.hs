
import Data.Array

main = do
    let a1 = array (0, 4) [(i,0) | i <- [0..4]]
    putStrLn $ "emp: " ++ show a1
    
    let a1' = a1 // [(4,100)]
    putStrLn $ "set: " ++ show a1'
    putStrLn $ "get: " ++ show (a1' ! 4)
    putStrLn $ "len: " ++ show ((+1) . snd . bounds $ a1')

    let a2 = array (0,4) [(i,i+1) | i <- [0..4]]
    putStrLn $ "dcl: " ++ show a2
    
    let a3 = array((0,0), (1,2)) [((i,j), i+j) | i <- [0..1], j <- [0..2]]
    putStrLn $ "2d:  " ++ show a3
