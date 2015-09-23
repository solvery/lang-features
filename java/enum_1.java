
public enum enum_1 {
	PLUS  { public double eval(double x, double y) { return x + y; } },
	MINUS { public double eval(double x, double y) { return x - y; } };
	public abstract double eval(double x, double y);
    public static void main(String[] args) {
		System.out.println(enum_1.PLUS.eval(1,1));
		System.out.println(enum_1.MINUS.eval(1,1));
    }
}


