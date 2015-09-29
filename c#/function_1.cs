
namespace CsharpExample {
	class Hello {
		static void Main() {
			string s = concat("Hello", ", ", "World", "!");
			System.Console.WriteLine(s);

			BMI(weight: 123, height: 64);
			BMI(height: 64, weight: 123);
		}

		public static string concat(params string[] args) {
			return System.String.Join("",args);
		}
		static int BMI(int weight, int height) {
			return (weight * 703) / (height * height);
		}
	}
}
