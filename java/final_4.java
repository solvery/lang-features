// final reference.

class ClassA {
	public int foo;

	public ClassA(int a) {
		foo = a;
	}
}

public class final_4 {
    public static void main(String[] args) {
		ClassA o1 = new ClassA(1);
		o1.foo = 2; 
		o1 = null;
		final ClassA o2 = new ClassA(1);
		o2.foo = 2; 
		/// o2 = null;
    }
}


