// inner class

public class oo_inner_class_3 {

	private int foo = 2;

	public class Inner1 {
		private int foo = 12;
		public void m1() {
			System.out.println("Inner1 m1");
			foo++;
			System.out.println(foo);
			System.out.println(this.foo);
			System.out.println(oo_inner_class_3.this.foo);
		};
	}

	public void m1() {
		System.out.println("oo_inner_class_3 m1");
	}

    public static void main(String[] args) {
		oo_inner_class_3 o1 = new oo_inner_class_3();
		Inner1 o2 = o1.new Inner1();
		o1.m1();
		o2.m1();
    }
}



