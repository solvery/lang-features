// inner class
// static inner class

public class oo_inner_class_1 {

	private int foo = 2;

	public void m2() {
		System.out.println("in m2");
		Inner1 in = new Inner1();
		in.m1();
	}
	public class Inner1 {
		private int foo = 12;
		private int v1;
		public void m1() {
			System.out.println("in m1");
		};
		public void m2() {
			foo++;
			System.out.println(foo);
			System.out.println(this.foo);
			System.out.println(oo_inner_class_1.this.foo);
		}
	}
	public static class Inner2 {
		private int v1;
		public void m1() {
			System.out.println("in m1");
		};
	}
	

    public static void main(String[] args) {
		oo_inner_class_1 o1 = new oo_inner_class_1();
		Inner1 o2 = o1.new Inner1();
		o1.m2();
		o2.m1();
		o2.m2();
		Inner2 o3 = new Inner2();
		o3.m1();
    }
}


