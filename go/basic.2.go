package main

import "fmt"
import "math"

func main() {
    fmt.Println("hello world")

    fmt.Printf("%t\n", 1==2)
    fmt.Printf("二进制：%b\n", 255)
    fmt.Printf("八进制：%o\n", 255)
    fmt.Printf("十六进制：%X\n", 255)
    fmt.Printf("十进制：%d\n", 255)
    fmt.Printf("浮点数：%f\n", math.Pi)
    fmt.Printf("字符串：%s\n", "hello world")

{
	//声明初始化一个变量
	var  x int = 100
	var str string = "hello world"</pre>
	//声明初始化多个变量
	var  i, j, k int = 1, 2, 3
	
	//不用指明类型，通过初始化值来推导
	var b = true //bool型
	
	x := 100 //等价于 var x int = 100;
	
	const s string = "hello world"
	const pi float32 = 3.1415926
}

// 数组
 {
    var a [5]int
    fmt.Println("array a:", a)

    a[1] = 10
    a[3] = 30
    fmt.Println("assign:", a)

    fmt.Println("len:", len(a))

    b := [5]int{1, 2, 3, 4, 5}
    fmt.Println("init:", b)

    var c [2][3]int
    for i := 0; i < 2; i++ {
        for j := 0; j < 3; j++ {
            c[i][j] = i + j
        }
    }
    fmt.Println("2d: ", c)

	a := [5]int{1, 2, 3, 4, 5}

b := a[2:4] // a[2] 和 a[3]，但不包括a[4]
fmt.Println(b)

b = a[:4] // 从 a[0]到a[4]，但不包括a[4]
fmt.Println(b)

b = a[2:] // 从 a[2]到a[4]，且包括a[2]
fmt.Println(b)


}

{
	// if 语句没有圆括号，而必需要有花括号

	//if 语句
	if x % 2 == 0 {
		//...
	}
	//if - else
	if x % 2 == 0 {
		//偶数...
	} else {
		//奇数...
	}

	//多分支
	if num < 0 {
		//负数
	} else if num == 0 {
		//零
	} else {
		//正数
	}
}

{
// switch语句没有break，还可以使用逗号case多个值

switch i {
    case 1:
        fmt.Println("one")
    case 2:
        fmt.Println("two")
    case 3:
        fmt.Println("three")
    case 4,5,6:
        fmt.Println("four, five, six")
    default:
        fmt.Println("invalid value!")
}
}

//经典的for语句 init; condition; post
for i := 0; i<10; i++{
     fmt.Println(i)
}

//精简的for语句 condition
i := 1
for i<10 {
    fmt.Println(i)
    i++
}

//死循环的for语句 相当于for(;;)
i :=1
for {
    if i>10 {
        break
    }
    i++
}


}
