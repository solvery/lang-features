// return this

public class oo_return_this_1 {
	public int num;
	public oo_return_this_1 grow() {
		num++;
		return this;
	}
    public static void main(String[] args) {
		oo_return_this_1 rt = new oo_return_this_1();
		rt.grow().grow().grow();
		System.out.println(rt.num);
    }
}


