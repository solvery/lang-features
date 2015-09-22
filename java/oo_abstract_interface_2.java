// abstract class implements interface

interface I {
	void m1();
}

abstract class A implements I {
}

class B extends A {
	public void m1(){
		System.out.println("B m1");
	}
}

class C extends A {
	public void m1(){
		System.out.println("C m1");
	}
}

public class oo_abstract_interface_2 {
    public static void main(String[] args) {
		A o1 = new B();
		A o2 = new C();
		o1.m1();
		o2.m1();
    }
}




