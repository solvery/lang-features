// create

class A{
	int v1 = 1;
	public int v2 = 2;

	public A(){
		System.Console.WriteLine("A A()");
	}
	public void m1(){
		System.Console.WriteLine("A m1");
	}
	public static void m2(){
		System.Console.WriteLine("A m2");
	}

}
class B:A {
}

class Hello {
	static void Main() {
		{
			A o1 = new A();
			/// System.Console.WriteLine(o1.v1);
			System.Console.WriteLine(o1.v2);
			o1.v2 = 3;
			System.Console.WriteLine(o1.v2);
			o1.m1();
			/// o1.m2();
			A.m2();
		}
		{
			B o1 = new B();
			System.Console.WriteLine(o1.v2);
		}
		{
			var o1 = new {s1="a", v1="1"};
			var o2 = new {s1="b", v1="2"};
			System.Console.WriteLine("{0} {1}", o1.s1, o1.v1);
		}

	}
}
