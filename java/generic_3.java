
class Foo<T super String> {
	public T a;
	public Foo(T a) {
		this.a = a;
	}
}

public class generic_3 {
	public static void main(String[] args) {
		Foo<String> o1 = new Foo<String>("foo");
		System.out.println(o1.a);
		/// Foo<Integer> o2 = new Foo<Integer>(2);
	}
}




