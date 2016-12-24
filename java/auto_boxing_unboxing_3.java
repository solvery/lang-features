// AutoBoxing and Unboxing（自动装箱&自动拆箱）
// Character类中自带一个静态的缓冲区，保存128个常用ASCII码字符对应的Character实例，免去每次重新构造实例的麻烦

import java.util.*;

public class auto_boxing_unboxing_2 {
    public static void main(String[] args) {
        Character ch1 = 'a'; 
        Character ch2 = Character.valueOf('a'); 
    }
}

