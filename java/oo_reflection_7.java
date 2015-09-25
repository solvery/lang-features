// call get/set method

import java.lang.reflect.*;

class A {
	private int v;
	public void setV(int a){
		this.v = a;
		System.out.println(v);
	}
	public int getV(){
		return this.v;
	}
}

public class oo_reflection_7 {
    public static void main(String[] args) throws Exception {
		Class<?> c1 = null;
		c1 = Class.forName("A");
		A o1 =  null;
		o1 = (A)c1.newInstance();

		setter(o1,"V", 2, int.class);

    }

	public static void setter(Object obj, String att, Object value, Class<?> type) throws Exception{
		Method method = obj.getClass().getMethod("set"+att, type);
		method.invoke(obj, value);
	}
}


