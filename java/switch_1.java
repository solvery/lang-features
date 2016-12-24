// switch的case语句可以处理int，short，byte，char类型的值，但是不能处理long，String等类型。
// 因为short，byte，char都会转换成int进行处理，这一点也可以从生成的字节码看出。

public class switch_1 {
    public static void main(String[] args) {
        byte  a = 1;
		int signum;
        switch(a) {
            case 0:
                signum = 0;
                break;
            case 1:
                signum = 1;
                break;
            default:
                signum = -1;
                break;
        }
        System.out.println(signum);
    }
}
