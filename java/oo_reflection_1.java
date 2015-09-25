
import java.lang.reflect.*;

public class oo_reflection_1 {
	public static void main(String[] args) {
		oo_reflection_1 o1 = new oo_reflection_1();
		System.out.println(o1.getClass());
		System.out.println(o1.getClass().getName());
		System.out.println(o1.getClass().getSuperclass());

		System.out.println(o1.getClass().getClassLoader().getClass());

	}
}


