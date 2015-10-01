
class C<U,V>{}
class D:C<string,int>{}
class E<U,V>:C<U,V>{}
class F<U,V>:C<string,int>{}
/// class G:C<U,V>{}

class Hello {
	static void Main() {
		System.Console.WriteLine();
	}
	void m1<T>(T a){}
	void m1<T>(T[] a){}
	void m1(int a){} // overload
	
	T m2<T>(T a){ return a;}
	void m1<T,V>(T a, V b){}
}
