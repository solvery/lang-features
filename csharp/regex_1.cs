using System.Text.RegularExpressions;

class Hello {
	static void Main() {
		{
			Regex regex = new Regex("ll");
			bool isMatch = regex.IsMatch("hello");
			System.Console.WriteLine(isMatch);
		}
		{
			Regex r1 = new Regex("ll");
			string s1 = r1.Replace("hello", "LL", 1);
			Regex r2 = new Regex("l");
			string s2 = r2.Replace("hello", "L");
			System.Console.WriteLine(s1);
			System.Console.WriteLine(s2);
		}
		{
		}
	}
}
