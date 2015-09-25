
import java.util.*;

enum E {
	A,B,C,D,E;
}

public class enum_hash_1 {
    public static void main(String[] args) {
		// EnumMap<E, String> em1 = new EnumMap<E, String>(E.class);
		// Map<E, String> em1 = new EnumMap<E, String>(E.class);
		Map<E, String> em1 = new EnumMap<E, String>(E.class);
		System.out.println(em1);

		em1.put(E.A, "a");
		em1.put(E.C, "c");
		System.out.println(em1);

		for (E e: E.values()) {
			System.out.println(e +" "+ em1.get(e));
		}
    }
}

