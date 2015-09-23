// interface as arg

interface I {
	public int m1();
}

public class oo_interface_4 {
	public void m2(I p) {
		System.out.println(p.m1());
	}
	public static void main(String[] args) {
		oo_interface_4 o1 = new oo_interface_4();
		o1.m2(new I() {
			public int m1(){
				return 2;
			}
		});
	}
}


