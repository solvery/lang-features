class Hello {
	static void Main() {
		System.Console.WriteLine();
		System.Console.WriteLine(string.Format("{0}: {1}", "Spain", 7));
		System.Console.WriteLine("hello".CompareTo("world"));
		System.Console.WriteLine("hello" + " world");
		System.Console.WriteLine("hello".ToUpper());
		System.Console.WriteLine("HELLO".ToLower());
		System.Console.WriteLine(" hello ".Trim());
		System.Console.WriteLine("hello".PadLeft(10));
		System.Console.WriteLine(14.ToString());
		System.Console.WriteLine(14.7.ToString());
		System.Console.WriteLine();
		System.Console.WriteLine(byte.Parse("65")   );
		System.Console.WriteLine(short.Parse("65")  );
		System.Console.WriteLine(int.Parse("65")    );
		System.Console.WriteLine(long.Parse("65")   );
		System.Console.WriteLine(float.Parse("65")  );
		System.Console.WriteLine(double.Parse("65") );
		System.Console.WriteLine(decimal.Parse("65"));
		System.Console.WriteLine();
		string[] names = "Bob Ned Amy".Split(' ');
		System.Console.WriteLine(System.String.Join(", ", names));
		System.Console.WriteLine();
		System.Console.WriteLine("hello".IndexOf("ll"));
		System.Console.WriteLine("hello".Substring(2, 2));
		System.Console.WriteLine();
		System.Console.WriteLine();

		char Char = 'A';
		System.Char.IsLetter(Char);
		System.Char.IsNumber(Char);
		System.Char.IsWhiteSpace(Char);
		System.Char.IsUpper(Char);
		System.Char.IsLower(Char);
	}
}

