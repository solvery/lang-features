
class Foo<A> {
	public A a;
	public Foo(A a) {
		this.a = a;
	}
}

public class generic_1 {
	public static void main(String[] args) {
		Foo<String> f = new Foo<String>("foo");
	}
}


