import java.lang.reflect.*;
import java.io.File;

public class oo_reflection_1 {
	public static void main(String[] args) {
		{
			Object o = new Object();
			Class c = o.getClass();
			String name = c.getName();
			Method[] m = c.getMethods();

		}
	}
}


