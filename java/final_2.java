// final method, cannot override

class Base {
	public final void m1() { }

	private final void m2() { }

	// overload
	public void m1(int a) { }
}

public class final_2 extends Base {

	// override
	public void m1() { }

	// ok
	public void m2() { }

    public static void main(String[] args) {
    }
}


