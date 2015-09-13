// final reference.

import java.util.Arrays;

public class final_5 {
	public static void main(String[] args) {
		final int[] iArr = {5, 6, 12, 9};
		System.out.println(Arrays.toString(iArr));
		Arrays.sort(iArr);
		System.out.println(Arrays.toString(iArr));
		iArr[2] = -8;
		System.out.println(Arrays.toString(iArr));
		/// iArr = null;
	}
}


