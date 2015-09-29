
class Hello {
	static void Main() {
		string s = m1("Hello", ", ", "World", "!");
		System.Console.WriteLine(s);

		//
		int v1;
		int v2;
		v1 = m2(a: 123, b: 64);
		v2 = m2(b: 64, a: 123);
		System.Console.WriteLine("{0} {1}", v1, v2);

		v1 = 1;
		v2 = 2;
		m3(ref v1, ref v2);
		System.Console.WriteLine("{0} {1}", v1, v2);
	}

	public static string m1(params string[] args) {
		return System.String.Join("",args);
	}
	static int m2(int a, int b) {
		return (a+b);
	}
	static void m3(ref int x, ref int y) {
		int temp = x;
		x = y;
		y = temp;
	}
}
