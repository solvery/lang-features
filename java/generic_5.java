// <T> T

public class generic_5 {
    public static void main(String[] args) {
		m1();
    }
	public static <T> T m1(){
		T v1 = null;
		return v1;
	}
	public static <T> void m2(){}
	public <T> void m3(){}
	/// public void m4(T[] a){}
	public <T> void m5(T[] a){
		for (T e: a) {
		}
	}
	public <T> void m6(T a){}
}

