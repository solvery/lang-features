import java.util.Arrays;
import java.lang.String;

public class string_1 {
	public static void main(String[] args) {
		{
			String s = "hello";
			String t = new String(s);
			String r = "hello" + " world";
		}
		{
			String s = "bar";
			StringBuffer sb = new StringBuffer(s);
			sb.setCharAt(2, 'z');
			String s2 = sb.toString();
		}
		{
			String.format("%s: %d", "Spain", 7);
			"hello".compareTo("world");
		}
		{
			char[] a = new char[80];
			Arrays.fill(a, '-');
			String s = new String(a);
		}
		{
			"hello".toUpperCase();
			"HELLO".toLowerCase();
			"hello".trim();
			Integer.toString(14);
			Long.toString(14);
			Double.toString(14.7);
			Byte.parseByte("14");
			Short.parseShort("14");
			Integer.parseInt("14");
			Long.parseLong("14");
			Float.parseFloat("14.7");
			Double.parseDouble("14.7");
			"Bob Ned Amy".split(" ");
			"hello".length();
			"hello".indexOf("ll");
			"hello".substring(2,4);
		}
		{
			Object hello = "Hello";
			System.out.println("字符串是否是Object类的实例：" + (hello instanceof Object));
			System.out.println("字符串是否是String类的实例：" + (hello instanceof String));
			System.out.println("字符串是否是Comparable接口的实例：" + (hello instanceof Comparable));
		}
		{
		}
	}
}


