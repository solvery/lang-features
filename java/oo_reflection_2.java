
public class oo_reflection_2 {
	public static void main(String[] args) {
		Class<?> c1 = null;
		Class<?> c2 = null;
		Class<?> c3 = null;

		try {
			c1 = Class.forName("oo_reflection_2");
		}catch(Exception e) {
			e.printStackTrace();
		}

		c2 = new oo_reflection_2().getClass();
		c3 = oo_reflection_2.class;

		System.out.println(c1.getName());
		System.out.println(c2.getName());
		System.out.println(c3.getName());
	}
}


