// star

class A {
	public string show(D obj) { return ("1 A and D"); }
	public string show(A obj) { return ("2 A and A"); }
}

class B : A {
	public string show(B obj) { return ("3 B and B"); }
	public string show(A obj) { return ("4 B and A"); }
}
class C : B {}
class D : B {}

class Hello {
	static void Main() {
		A a1 = new A();
		A a2 = new B();
		B b = new B();
		C c = new C();
		D d = new D();
		System.Console.WriteLine(a1.show(b));
		System.Console.WriteLine(a1.show(c));
		System.Console.WriteLine(a1.show(d));
		System.Console.WriteLine(a2.show(b));
		System.Console.WriteLine(a2.show(c));
		System.Console.WriteLine(a2.show(d));
		System.Console.WriteLine( b.show(b));
		System.Console.WriteLine( b.show(c));
		System.Console.WriteLine( b.show(d));
	}
}
// 2 A and A
// 2 A and A
// 1 A and D
// 2 A and A
// 2 A and A
// 1 A and D
// 3 B and B
// 3 B and B
// 3 B and B

