// length 针对数组
// length 针对String 
// size 针对泛型集合

import java.util.*;

public class length_1 {
    public static void main(String[] args) {
        int[] a1 = new int[10];
        System.out.println(a1.length);
        // System.out.println(a1.length()); // error

        System.out.println("hello".length());
        // System.out.println("hello".length); // error
        
        List<Integer> array=new ArrayList<Integer>();
        array.add(1);
        array.add(2);
        array.add(3);
        System.out.println(array.size());

    }
}


