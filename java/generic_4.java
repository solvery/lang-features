// wildcard

class Foo<T> {
	public T a;
	public Foo(T a) {
		this.a = a;
	}
}

public class generic_4 {
	public static void main(String[] args) {
		Foo<String> o1 = new Foo<String>("foo");
		System.out.println(o1.a);
		Foo<Integer> o2 = new Foo<Integer>(2);
		System.out.println(o2.a);

		m1(o1);
		m1(o2);

		m2(o1);
		/// m2(o2);

		m3(o1);
	}

	public static void m1(Foo<?> f) {
		System.out.println(f.a);
	}
	public static void m2(Foo<? extends String> f) {
		System.out.println(f.a);
	}
	public static void m3(Foo<? super String> f) {
		System.out.println(f.a);
	}
}



