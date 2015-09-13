// final as variable
// final with static
// final as args

public class final_3 {
	public int v1;
	public int v2 = 2;

	public final int fv1 = 1;
	public final static int fv3 = 3;

	private final int fv5;
	private final static int fv6;

	public final String s1 = "hello";

	// inital in object create
	public final int fv2;
	/// public final static int fv4;

	{
		fv5 = 5;
	}

	static {
		fv6 = 6;
	}
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

