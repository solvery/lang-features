// call method

import java.lang.reflect.*;

class A {
	public void m1(){
		System.out.println("A m1");
	}
}

public class oo_reflection_6 {
    public static void main(String[] args) throws Exception {
		Class<?> c1 = null;
		c1 = Class.forName("A");

		Method m1 = c1.getMethod("m1");
		m1.invoke(c1.newInstance());
    }
}

