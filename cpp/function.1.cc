#include <iostream>
#include <cmath>

using namespace std;

// declare
int
add(int m, int n);

// define
int
add(int m, int n) {
	return m + n;
}

// overload
float add(float x, float y) {
	return x + y;
}

// overload operator

// static class method
class Ops {
	public:
		static int add(int m, int n);
};
int Ops::add(int m, int n) {
	return m + n;
}

// default args
float
logarithm(float x, float base = 10.0) {
	return log(x) / log(base);
}

// args by value, reference, address
int add1(int n) {
	return ++n;
}
int add2(int& n) {
	return ++n;
}
int add3(int* n) {
	return ++*n;
}

// recursive 
int
factorial(int n) {
	if (n <= 1) {
		return 1;
	}
	return n * factorial(n - 1);
}

// anonymous 
auto add4 = [](int n, int m) {
	return n + m;
};

int main(int argc, char** arg) {
	{
		int sum = add(3, 7);
		sum = Ops::add(3, 7);
	}
	{
		int i(7);
		int i1 = add1(i);
		int i2 = add2(i);
		int i3 = add3(&i);
	}
	{
		int sum = add4(3, 7);
		int sum2 = [](int n, int m) {
			return n + m;
		}(3, 7);
	}
	{
	}
}


