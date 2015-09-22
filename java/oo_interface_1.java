
interface I {
	void m1();
}

class A implements I {
	public void m1() {
		System.out.println("A m1");
	}
}

public class oo_interface_1 {
    public static void main(String[] args) {
		A o1 = new A();
		o1.m1();
    }
}


