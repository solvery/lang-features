// to get implemented interface

interface I1 { }
interface I2 { }

class A implements I1, I2 {
}

public class oo_reflection_5 {
    public static void main(String[] args) throws Exception {
		Class<?> c1 = null;
		c1 = Class.forName("A");
		Class<?> ifs[] = c1.getInterfaces();

		for(Class<?> e: ifs) {
			System.out.println(e.getName());
		}
    }
}


