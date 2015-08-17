
package main
import "fmt"

func f(msg string) {
    fmt.Println(msg)
}

func main(){
    go f("goroutine")

	// 匿名函数
    go func(msg string) {
        fmt.Println(msg)
    }("going")
}
