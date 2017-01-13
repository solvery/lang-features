

public class goto_1 {
    public static void main(String[] args) {
        pos1:
        for (int i=0; i<5; i++)
        {
            System.out.println("Hello world");
            continue pos1;
        }
    }
}


