class Hello {
	static void Main() {
		{
			int i;
			int j = 3;
			const int k = 2;
			object o = 0;
		}
		{
			string s2 = "a";
			string s1 = s2 ?? "was null";
			System.Console.WriteLine(s1);
		}
		{
			int i = 0;
			int signum;
			if (i>0) {
				signum = 1;
			} else if (i==0) {
				signum = 0;
			} else {
				signum = -1;
			}

			switch(i) {
				case 0:
					break;
				case 1:
					break;
				default:
					break;
			}
		}
		{
			int i = 123;
			object o = i;	// boxing
			int j = (int)o; // unboxing
			System.Console.WriteLine(j);
		}
	}
}

