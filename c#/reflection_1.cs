
class Hello {
	static void Main() {
		object o = new object();
		System.Type t1 = o.GetType();
		System.Type t2 = typeof(object);
		System.Console.WriteLine(t1);
		System.Console.WriteLine(t2);
		System.Console.WriteLine(t2.ToString());
	}
}
