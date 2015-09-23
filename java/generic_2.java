
class Foo<T> {
	public T a;
	public Foo(T a) {
		this.a = a;
	}
}

public class generic_2 {
	public static void main(String[] args) {
		Foo<String> o1 = new Foo<String>("foo");
		System.out.println(o1.a);
		Foo<Integer> o2 = new Foo<Integer>(2);
		System.out.println(o2.a);
	}
}



