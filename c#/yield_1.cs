
using System;
using System.Collections.Generic;

class Hello {
	static IEnumerable<int> Range(int from, int to){
		for (int i = from; i < to; i++) {
			yield return i;
		}
		yield break;
	}
	static void Main() {
		foreach (int x in Range(-5,5)) {
			Console.WriteLine(x);
		}
	}
}
