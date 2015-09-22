// abstract with own data and method.

abstract class A {
	public abstract void m1();
	int v1;
	public void m2(){
		System.out.println("A m2");
	}
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

public class oo_abstract_2 {
    public static void main(String[] args) {
		A o1 = new B();
		A o2 = new C();
		o1.m1();
		o2.m1();
		o2.m2();
    }
}



