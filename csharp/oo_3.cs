
class A1 {
	public int v1{
		get { 
			return _v1;
		}
		set { 
			_v1 = value; 
		}
	}
	public int _v1 = 2;
}

class Hello {
	static void Main() {
		A1 o1 = new A1();
		System.Console.WriteLine(o1.v1);
	}
}
