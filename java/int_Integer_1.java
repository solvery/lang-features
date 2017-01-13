// AutoBoxing and Unboxing（自动装箱&自动拆箱）

import java.util.*;

public class int_Integer_1 {
    public static void main(String[] args) {
        ArrayList<Integer> array_list=new ArrayList<Integer>();

        int num_int=40;
        Integer num_integer =new Integer(num_int);

        array_list.add(num_int);
        array_list.add(num_integer);
    }
}
