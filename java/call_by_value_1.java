// = 修改了内存状态
// 参数传递相当于一种=操作

public class call_by_value_1 {
    void func1(int value) {
        value = 100;
    }

    void func2(String text) {
        text = "windows";
    }

    void func3(StringBuilder builder) {
        builder.append(" world");
    }

    void func4(StringBuilder builder) {
        builder = new StringBuilder("hehe");
    }

    public static void main(String[] args) {
        call_by_value_1 o1 = new call_by_value_1();
        int num = 10;
        o1.func1(num);
        System.out.println(num);

        String s = "hello";
        o1.func2(s);
        System.out.println(s);

        StringBuilder sb = new StringBuilder("hello");
        o1.func3(sb); // 改变了
        System.out.println(sb);

        o1.func4(sb);
        System.out.println(sb);
    }
}

