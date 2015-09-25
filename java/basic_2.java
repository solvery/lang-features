
public class basic_2 {
	public static void main(String[] args) {
		{
			int i;
			int j = 3;
		}
		{
			final int i = 7;
			int n;
			n = 3;
		}
		{
			int n = 1;
			int one = n++;
			int three = ++n;
			int two = --n;
		}
		{
			Integer i = new Integer(0);
		}
		{
			String s2 = "hello";
			String s1 = s2 == null ? "was null" : s2;
		}
		{
			Math.pow(2.0, 32.0);
			Math.sqrt(2);
			long l;
			l = (long)3.77;
			Math.round(3.77);
			l = (long)Math.floor(3.77);
			l = (long)Math.ceil(3.77);
			Math.abs(-7);
			Math.abs(-7.77);
		}
		{
			boolean b1 = true;
			boolean b2 = false;
			// boolean to string
			String str = true + "";
			System.out.println(str); 
		}
		{
			float af = 5.2345556f;
			System.out.println(af);
			double a = 0.0;
			double c = Double.NEGATIVE_INFINITY;
			float d = Float.NEGATIVE_INFINITY;
			System.out.println(c == d);
			//0.0除以0.0将出现非数
			System.out.println(a / a);
			//两个非数之间是不相等的
			System.out.println(a / a == Float.NaN);
			//所有正无穷大都是相等的
			System.out.println(6.0 / 0 == 555.0/0);
			//负数除以0.0得到负无穷大
			System.out.println(-8 / a);
			//下面代码将抛出除以0的异常
			//System.out.println(0 / 0);
		}
		{
			byte a = 56;
			long bigValue2 = 9223372036854775807L;
			byte b = 9;
			// 下面代码将出错，byte型不能自动类型转换为char型
			//char c = b;

		}
		{

			System.out.println("Hello!" + 'a' + 7);
			System.out.println('a' + 7 + "Hello!");
			System.out.println(3 + 4 + "Hello！");
			System.out.println("Hello！" + 3 + 4);
			int a; int b; int c;
			a = b = c = 7;
			System.out.println(5 & 9);
			System.out.println(5 | 9);
			System.out.println(~-5);
			System.out.println(5 ^ 9);
			System.out.println(5 << 2);
			System.out.println(-5 << 2);
			System.out.println(-5 >> 2);
			System.out.println(-5 >>> 2);
			System.out.println("5和5.0是否相等：" + (5 == 5.0));
			System.out.println("97和'a'是否相等：" + (97 == 'a'));
			System.out.println("true和false是否相等：" + (true == false));
			a = new Integer(6);
			//通过自动装箱，允许把基本类型值赋值给包装类的实例
			Integer ina = 2;
			Integer inb = 2;
			System.out.println("两个2自动装箱后是否相等：" + (ina == inb));
			Integer biga = 128;
			Integer bigb = 128;
			//输出false
			System.out.println("两个128自动装箱后是否相等：" + (biga == bigb));
		}
		{
			System.out.println(System.getProperty("java.runtime.version"));
		}
	}
}


