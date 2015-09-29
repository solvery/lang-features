// poly, this > super > this(super) > super(super)
// star

class A {
	public String show(D obj) { return ("1 A and D"); }
	public String show(A obj) { return ("2 A and A"); }
}

class B extends A {
	public String show(B obj) { return ("3 B and B"); }
	public String show(A obj) { return ("4 B and A"); }
}
class C extends B {}
class D extends B {}

public class oo_poly_1 {
    public static void main(String[] args) {
		A a1 = new A();
		A a2 = new B();
		B b = new B();
		C c = new C();
		D d = new D();
		System.out.println(a1.show(b));
		System.out.println(a1.show(c));
		System.out.println(a1.show(d));
		System.out.println(a2.show(b));
		System.out.println(a2.show(c));
		System.out.println(a2.show(d));
		System.out.println( b.show(b));
		System.out.println( b.show(c));
		System.out.println( b.show(d));

		System.out.println(a1 instanceof B);
		System.out.println(a2 instanceof A);
		System.out.println(a2 instanceof B);
		System.out.println( b instanceof B);
		System.out.println( b instanceof A);
    }
}

// 2 A and A
// 2 A and A
// 1 A and D
// 4 B and A
// 4 B and A
// 1 A and D
// 3 B and B
// 3 B and B
// 1 A and D
