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

int add1(int n) {
	return ++n;
}
int add2(int& n) {
	return ++n;
}
int add3(int* n) {
	return ++*n;
}


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
	}
	{
	}
}


