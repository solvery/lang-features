// AutoBoxing and Unboxing（自动装箱&自动拆箱）
// auto_boxing_unboxing_1 效率改进

import java.util.*;

public class auto_boxing_unboxing_2 {
    public static void main(String[] args) {
        Long sum = 0L;
        long s = sum;
        for (long i = 0; i < Integer.MAX_VALUE; i++) {
            s += i;   
        }
        sum = Long.valueOf(s);
        System.out.println(sum);
    }
}
