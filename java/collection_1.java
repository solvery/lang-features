
import java.util.*;

public class collection_1 {
    public static void main(String[] args) {
		// Collection<String> c1 = new HashSet<String>();
		// Collection<String> c1 = new LinkedHashSet<String>();
		// Collection<String> c1 = new ArrayList<String>();
		// Collection<String> c1 = new TreeSet<String>();
		// Collection<String> c1 = new Stack<String>();
		// Collection<String> c1 = new PriorityQueue<String>();
		Collection<String> c1 = new PriorityQueue<String>();

		// Set<String> c1 = new HashSet<String>();
		// HashSet<String> c1 = new HashSet<String>();
		// LinkedHashSet<String> c1 = new LinkedHashSet<String>();
		
		// List<String> c1 = new ArrayList<String>();

		
		c1.add("a");
		c1.add("b");
		c1.add("c");
		System.out.println(c1.size());

		// 1
		Iterator<String> iter = c1.iterator();
		while (iter.hasNext()) {
			System.out.println(iter.next());
		}
		System.out.println();
		// 2
		for(String e:c1) {
			System.out.println(e);
		}
		System.out.println();
		// 3
		System.out.println(c1);

	}
}


