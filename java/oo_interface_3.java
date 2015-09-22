
interface I {
	void m1();
}
interface J extends I {
	void m1();
}

class A implements I, J {
	public void m1() {
		System.out.println("A m1");
	}
}

public class oo_interface_3 {
    public static void main(String[] args) {
		A o1 = new A();
		o1.m1();
    }
}




