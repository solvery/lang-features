
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
			for ( Map.Entry<String, Integer> e : m.entrySet() ) {
				  e.getKey(); 
				  e.getValue();
			}
			System.out.println(m);
		}
    }
}


