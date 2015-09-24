
import java.util.*;

enum E {
	A,B,C
}

public class set_1 {
    public static void main(String[] args) {
		EnumSet<E> es1 = EnumSet.allOf(E.class);
		System.out.println(es1);

		EnumSet<E> es2 = EnumSet.noneOf(E.class);
		es2.add(E.X);
		es2.add(E.Y);
		System.out.println(es2);
    }
}

