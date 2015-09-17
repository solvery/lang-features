
public class array_1 {
	public static void main(String[] args) {
		{
			// arrays must be allocated on heap
			// error: int a[10];
			// garbage collected
			// error: delete[] a;
			int[] a1 = new int[10];
			int[] intArr;
			intArr = new int[]{5, 6, 8 , 20};
			Object[] books = new String[4];
		}
		{
			int[] a = {5, 6 , 7, 9};
			for (int i = 0 ; i < a.length ; i++ )
			{
				System.out.println(a[i]);
			}
		}
{
		int[] a = new int[]{3, 4 , 5, 6};
		int[] b = Arrays.copyOf(a, 6); 
		Arrays.fill(b , 2, 4 , 1);
		Arrays.sort(b);
}
		{
			java.util.Vector<String> vec = new java.util.Vector<String>();
			vec.size();
			//vec.elementAt(0);
			vec.add("hello");
			vec.add(vec.size(), "hello");
			vec.removeElementAt(vec.size()-1);
		}
		{
			String[] books = {"book1", "book2", "book3"};
			for (String book : books) {
				System.out.println(book);
			}

		}
		{
		}
		{
		}
		{
		}
		{
		}
		{
		}
	}
}


