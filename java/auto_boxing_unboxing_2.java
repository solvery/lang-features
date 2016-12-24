// AutoBoxing and Unboxing（自动装箱&自动拆箱）

import java.util.*;

public class auto_boxing_unboxing_1 {
    public static void main(String[] args) {
        Long sum = 0L;
        for (long i = 0; i < Integer.MAX_VALUE; i++) {
            sum += i;   
        }
        System.out.println(sum);
    }
}
