
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

class Hello {
	static void Main() {
		A o1 = new A();
		/// System.Console.WriteLine(o1.v1);
		System.Console.WriteLine(o1.v2);
		o1.m1();
		/// o1.m2();
		A.m2();
	}
	{
		var patent1 =
			new { Title = "Bifocals",
				YearOfPublication = "1784" };
		var patent2 =
			new { Title = "Phonograph",
				YearOfPublication = "1877" };
	}
}
