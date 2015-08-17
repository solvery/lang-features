package main 
import "fmt"
import "os"

var user = os.Getenv("USER")
func main() {
    if user == "" {
        panic("no value for $USER")
    }
	fmt.Printf("what?\n")
}
