
import java.util.*;

class A {
	public int v;
	public A(int v) {
		this.v = v;
	}

	public String toString(){
		return v+"";
	}
}

public class collection_3 {
    public static void main(String[] args) {
		List<A> c1 = Arrays.asList(
				new A(1),
				new A(2),
				new A(3),
				new A(5));
		System.out.println(c1);
	}
}
