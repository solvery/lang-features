
public class garbage_collection_1 {
    public static void main(String[] args) {
		for (int i=0; i<4; i++) {
			new garbage_collection_1();
			Runtime.getRuntime().gc();
			//System.gc();
		}
    }
	public void finalize() {
		System.out.println("gc...");
	}
}


