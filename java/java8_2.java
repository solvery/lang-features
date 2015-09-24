// mixin, Scala trait

interface I {
	void m1();
	default void m2(){
		System.out.println("I m2");
	}
}

public class java8_2 {
    public static void main(String[] args) {
		I o1 = new I() {
			public void m1() {
				System.out.println("m1");
			}
		};
		o1.m1();
		o1.m2();
    }
}


