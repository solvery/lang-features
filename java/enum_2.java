
public enum enum_2 {
	PLUS, MINUS;
	public double eval(double x, double y) {
		switch(this) {
			case PLUS:	return x + y;
			case MINUS:	return x - y;
			default: return 0;
		}
	}
    public static void main(String[] args) {
		System.out.println(enum_2.PLUS.eval(1,1));
		System.out.println(enum_2.MINUS.eval(1,1));
    }
}



