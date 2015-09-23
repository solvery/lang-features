// static class

public class oo_2 {
	static class A {
		private static int v1 = 5;
		private int v2 = 2;
	}
    public static void main(String[] args) {
		System.out.println(A.v1);
		/// System.out.println(A.v2);
		System.out.println(new A().v1);
		System.out.println(new A().v2);
    }
}


