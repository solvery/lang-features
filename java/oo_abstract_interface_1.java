
interface I {
	void m1();
}

abstract class A {
	public abstract void m1();
}

class B extends A implements I {
	public void m1(){
		System.out.println("B m1");
	}
}

class C extends A {
	public void m1(){
		System.out.println("C m1");
	}
}

public class oo_abstract_interface_1 {
    public static void main(String[] args) {
		A o1 = new B();
		A o2 = new C();
		o1.m1();
		o2.m1();
    }
}



