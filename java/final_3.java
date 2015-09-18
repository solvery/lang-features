// final as variable
// final with static
// final as args

public class final_3 {
	public int v1;
	public int v2 = 2;

	public final int fv1 = 0;
	public final static int fv3 = 0;
	//public final static int fv5;
	private final int fv5;

	public final String s1 = "hello";

	// inital in object create
	public final int fv2;
	/// public final static int fv4;

	public final_3(int a) {
		fv2 = a;
	}

	public void m1(final int a) {
		System.out.println(a);
	}

    public static void main(String[] args) {
		final_3 o1 = new final_3(2);
		o1.m1(3);
		/// final double fv6;
		/// fv6 = 1;
    }
}

