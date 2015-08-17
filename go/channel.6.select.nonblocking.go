package main
import "time"
import "fmt"

func main() {
    //创建两个channel - c1 c2
    c1 := make(chan string)
    c2 := make(chan string)
    var timeout_cnt int = 0

    //创建两个goruntine来分别向这两个channel发送数据
    go func() {
        time.Sleep(time.Second * 1)
        c1 <- "Hello"
    }()
    go func() {
        time.Sleep(time.Second * 1)
        c2 <- "World"
    }()

    //使用select来侦听两个channel
    for {
        select {
        case msg1 := <-c1:
            fmt.Println("received", msg1)
        case msg2 := <-c2:
            fmt.Println("received", msg2)
        default: //default会导致无阻塞
            fmt.Println("nothing received!")
            time.Sleep(time.Second)
        }
    }
}
