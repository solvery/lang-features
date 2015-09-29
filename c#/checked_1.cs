
using System;

class Hello {
	static void Main() {
		System.Console.WriteLine();
		int i = int.MaxValue;
		checked {
			Console.WriteLine(i + 1);		// Exception
		}
		unchecked {
			Console.WriteLine(i + 1);		// Overflow
		}
	}
}
