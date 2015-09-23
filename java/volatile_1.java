
public class volatile_1 extends Thread {

	//共享变量
	//private static volatile boolean flag = false;
	private static boolean flag = false;

	//无限循环读共享变量
	public void run() {
		while (!flag) {
			System.out.println(this + ":" + System.currentTimeMillis());
		}
	}

	public static void main(String[] args) throws Exception {
		for (int i = 0; i < 300; i++) {
			new volatile_1().start();
		}
		Thread.sleep(100);
		flag = true;
	}


}
