
class Foo<T> {
	public T a;
	public Foo(T a) {
		this.a = a;
	}
}

class Hello {
	static void Main() {
		Foo<string> o1 = new Foo<string>("hello");
		System.Console.WriteLine(o1.a);
		Foo<int> o2 = new Foo<int>(2);
		System.Console.WriteLine(o2.a);
	}
}
