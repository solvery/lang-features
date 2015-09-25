
import java.util.*;

public class collection_2 {
    public static void main(String[] args) {
		List<Integer> c1 = Arrays.asList(1,2,3,4,5,-1,-2,0,0);
		System.out.println(c1);
		System.out.println(Collections.binarySearch(c1, 5));
		Collections.shuffle(c1);
		System.out.println(c1);
		Collections.sort(c1);
		System.out.println(c1);

		List<Integer> c2 = Collections.nCopies(10, 5);
		System.out.println(c2);
	}
}
