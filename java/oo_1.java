
class BaseClass {
	public int foo = 5;
}

public class oo_1 extends BaseClass {
	public int foo;

	// constractor
	public oo_1() {
		int foo = 0;
		this.foo = 6;
	}

	// overload
	public void test() {
		System.out.println("no args");
	}
	public void test(String msg) {
		System.out.println("" + msg);
	}
	public void test(String... msg ) {
		for (String s : msg) {
			System.out.println(s);
		}
	}

	// super
	public void accessBase() {
		System.out.println(super.foo);
	}
	
    public static void main(String[] args) {
		oo_1 o1 = new oo_1();
		oo_1 o2;
		o2 = new oo_1();
		System.out.println(new oo_1().foo);
		o2.test();
		o2.test("hello");
		o2.test(new String[]{"he","he"});
		o2.accessBase();
    }
}


