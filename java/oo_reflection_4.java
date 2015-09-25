
import java.lang.reflect.Constructor;

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
		// get all constructor
		Constructor<?> cons[] = c1.getConstructors();
		o1 = (A)cons[0].newInstance();
		o2 = (A)cons[1].newInstance(1);
		o3 = (A)cons[2].newInstance(1,2);

		for(Constructor<?> e: cons) {
			System.out.println(e);
		}
    }
}



