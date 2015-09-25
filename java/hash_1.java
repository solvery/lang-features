
import java.util.*;

public class hash_1 {
    public static void main(String[] args) {
		{
			// TreeMap<String, Integer> m = new TreeMap<String, Integer>();
			// TreeMap<String, Integer> m = new HashMap<String, Integer>();
			// TreeMap<String, Integer> m = new Hashtable<String, Integer>();
			Map<String, Integer> m = new Hashtable<String, Integer>();
			m.put("foo", 2);
			m.put("hello", 5);
			m.get("hello");

			m.size();
			m.remove("hello");

			Iterator<String> it = m.keySet().iterator();
			String first = it.next();
			System.out.println(first);

			Iterator<Integer> it2 = m.entrySet().iterator();
			while (m.hasNext()) {
				Map.Entry<String, Integer> e = it2.next();
				System.out.println(e);
			}

			for ( Map.Entry<String, Integer> e : m.entrySet() ) {
				  e.getKey(); 
				  e.getValue();
			}
			System.out.println(m);
		}
    }
}


