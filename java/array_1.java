
public class array_1 {
	public static void main(String[] args) {
		{
			// arrays must be allocated on heap
			// error: int a[10];
			// garbage collected
			// error: delete[] a;
			int[] a = new int[10];
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
		}
		{
		}
    }
}


