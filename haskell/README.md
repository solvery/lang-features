
run:
	runhaskell xxx.hs

sign:
    ' :: : ++ -> <-
    函数名最后的那个单引号，它没有任何特殊含义，只是一个函数名的合法字符罢了
    :: 声明类型
    ++ list合并
    : 运算符往一个List前端插入元素
        :运算符可以连接一个元素到一个List或者字符串之中，而++运算符则是连接两个List
        [1,2,3]实际上是1:2:3:[]的语法糖
    !! 按照索引取得List中的元素
    List中的List可以是不同长度，但必须得是相同的类型


ghc
ghci
	:l myfunctions.hs

