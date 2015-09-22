// inner class

public class oo_inner_class_2 {

	public class Inner1 {
		public void m1() {
			System.out.println("Inner1 m1");
		};
	}

	public void m1() {
		System.out.println("oo_inner_class_2 m1");
	}
	public void m2() {
		System.out.println("oo_inner_class_2 m2");
	}

    public static void main(String[] args) {
		oo_inner_class_2 o1 = new oo_inner_class_2();
		Inner1 o2 = o1.new Inner1();
		o1.m1();
		o1.m2();
		o2.m1();
		/// o2.m2();
    }
}



