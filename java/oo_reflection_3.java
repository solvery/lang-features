
class A{
}

public class oo_reflection_3 {
    public static void main(String[] args) throws Exception {
		Class<?> c1 = null;
		c1=Class.forName("A");

		A o1 =  null;
		o1 = (A)c1.newInstance();
    }
}


