
import java.util.*;

public class collection_1 {
    public static void main(String[] args) {
		Collection<String> c1 = new ArrayList<String>();

		Collection<String> c2 = new HashSet<String>();
		Collection<String> c3 = new LinkedHashSet<String>();
		Collection<String> c4 = new ArrayList<String>();
		Collection<String> c5 = new TreeSet<String>();
		Collection<String> c6 = new Stack<String>();
		Collection<String> c7 = new PriorityQueue<String>();

		Set<String> c9 = new HashSet<String>();
		HashSet<String> c10 = new HashSet<String>();
		LinkedHashSet<String> c11 = new LinkedHashSet<String>();
		
		List<String> c12 = new ArrayList<String>();

		Collection<String> c13 = Collections.synchronizedCollection(new ArrayList<String>());
		List<String> c14 = Collections.synchronizedList(new ArrayList<String>());

		List<String> c15 = Collections.emptyList();
		List<?> c16 = Collections.emptyList();

		
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


