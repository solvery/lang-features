
public class basic_3 {
	public static void main(String[] args) {
		int i = 0;
		int signum;
		{
			if (i>0) {
				signum = 1;
			} else if (i==0) {
				signum = 0;
			} else {
				signum = -1;
			}
		}
		{
			switch(i) {
				case 0:
					signum = 0;
					break;
				case 1:
					signum = 1;
					break;
				default:
					signum = -1;
					break;
			}
		}
		{
			while (i<10) {
				i++;
			}
		}
		{
			int n = 1;
			for (i=1; i<=10; i++) {
				n *= i;
			}
		}
	}
}
