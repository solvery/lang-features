
import java.util.*;

enum E {
	A,B,C,D,E //;
}

public class enum_set_1 {
    public static void main(String[] args) {
		// EnumSet<E> es1 = EnumSet.allOf(E.class);
		// Set<E> es1 = EnumSet.allOf(E.class);
		Set<E> es1 = EnumSet.allOf(E.class);
		System.out.println(es1);

		EnumSet<E> es2 = EnumSet.noneOf(E.class);
		es2.add(E.A);
		es2.add(E.B);
		System.out.println(es2);

		EnumSet<E> es3 = EnumSet.of(E.A, E.B);
		System.out.println(es3);

		EnumSet<E> es4 = EnumSet.range(E.A, E.C);
		System.out.println(es4);

		EnumSet<E> es5 = EnumSet.complementOf(es4);
		System.out.println(es5);
    }
}

