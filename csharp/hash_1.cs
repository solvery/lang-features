
using System.Collections.Generic;

class Hello {
	static void Main() {
		System.Console.WriteLine();
		{
			KeyValuePair<string,int> pr = new KeyValuePair<string,int>("hello",5);
			System.Console.WriteLine("{0} {1}", pr.Key, pr.Value);
		}
		{
			Dictionary<string, int> dict = new Dictionary<string, int>();
			dict.Add("hello", 5);
			System.Console.WriteLine(dict["hello"]);
			dict.Remove("hello");

			dict.Add("a", 1);
			dict.Add("b", 2);
			foreach (KeyValuePair<string,int> e in dict) {
				System.Console.WriteLine(e.Key, e.Value);
			}

		}
	}
}
