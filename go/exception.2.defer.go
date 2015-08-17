// Go语言引入了Defer来确保那些被打开的文件能被关闭。
// Go的defer语句预设一个函数调用（延期的函数），该调用在函数执行defer返回时立刻运行。
// 无论函数怎样返回，都必须进行资源释放。

package main 
import "fmt"

func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }
    defer src.Close()

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }
    defer dst.Close()

    return io.Copy(dst, src)
}
