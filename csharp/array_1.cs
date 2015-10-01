
class Hello {
	static void Main() {
		{
			string[] s1 = {"a","b","c"};
			string[] s2;
			s2 = new string[] {"a","b","c"};
			string[] s3 = new string[] {"a","b","c"};
			string[] s4 = new string[3] {"a","b","c"};
			string[] s5 = new string[3];
		}
		{
			int[,] a1 = new int[3,3];
			int[,] a2 = {
				{1, 0, 2},
				{1, 2, 0},
				{1, 2, 1}
			};
			a2[1,2] = 3;
            int[][] a3 = {
                new int[] {1, 0, 2, 0},
                new int[] {1, 2, 0},
                new int[] {1, 2},
                new int[] {1}
            };
			/// a3[1,2] = 3;
			a3[1][2] = 3;
			/// a3[1][9] = 3; // bounds check
		}
	}
}
