
public class volatile_2 {

	//jprivate volatile int i = 0;
	//jprivate volatile int j = 0;
	private int i = 0;
	private int j = 0;
	public long exceptionCount = 0;

	public void f1() {
		for(int k = 0; k < Integer.MAX_VALUE; k++) {
			i = k;
			j = i;
		}
	}

	public void f2() {
		while (true) {
			if(j > i) {
				exceptionCount++;
			}
		}
	}

	public static void main(String[] args) {
		final volatile_2 volatileTest = new volatile_2();
		new Thread(new Runnable() {
				@Override
				public void run() {
				volatileTest.f1();
				}
				}).start();
		new Thread(new Runnable() {
				@Override
				public void run() {
				volatileTest.f2();
				}
				}).start();
		try {
			Thread.sleep(5000);
		} catch (InterruptedException e) {

		}
		System.out.println("exceptionCount:" + volatileTest.exceptionCount);
	}
}

