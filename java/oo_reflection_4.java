
class A{
	public int v1;
	public int v2;
	public A(){}
	public A(int a){
		this.v1 = a;
	}
	public A(int a, int b){
		this.v1 = a;
		this.v2 = b;
	}
}

public class oo_reflection_4 {
    public static void main(String[] args) throws Exception {
		Class<?> c1 = null;
		c1=Class.forName("A");

		A o1 =  null;
		A o2 =  null;
		A o3 =  null;
		o1 = (A)c1.newInstance();
    }
}



