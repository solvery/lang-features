
using System.Collections.Generic;

class Hello {
	static void Main() {
		{
			List<string> l = new List<string>();
			l.Add("hello");
			l.RemoveAt(l.Count - 1);
			System.Console.WriteLine(l.Count);
			l.Add("a");
			l.Add("b");
			l.Add("c");
			System.Console.WriteLine(l.Count);

			foreach (string s in l) {
				System.Console.WriteLine(s);
			}
		}
	}
}

