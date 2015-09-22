// anyomous local class

public class oo_local_class_3 {
	public final int fv1 = 1;
	public int v1 = 2;

	public void m1() {
		final int fv2 = 3;
		int v2 = 4;
		String s1 = "hello";

		return new Local1(){
			public void m1() {
				System.out.println("Local1 m1");
				System.out.println(fv1);
				System.out.println(v1);
				System.out.println(fv2);
				System.out.println(v2);
				System.out.println(s1);
			}
		};
	}
	public static void main(String[] args) {
		oo_local_class_3 o1 = new oo_local_class_3();
		o1.m1();
	}
}




