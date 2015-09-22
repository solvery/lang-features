
public class oo_local_class_1 {
	public void m1() {
		class Local1 {
			public void m1() {
				System.out.println("Local1 m1");
			}
		}
		new Local1().m1();
	}
    public static void main(String[] args) {
		oo_local_class_1 o1 = new oo_local_class_1();
		o1.m1();
    }
}


