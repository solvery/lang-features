
#include <iostream>

using namespace std;

template <class T>
inline T square(T x) {
	T result;
	result = x*x;
	return result;
}

int main(int argc, char** arg) {
	int v1 = 2;
	float v2 = 2.2;
	double v3 = 2.2;

	cout << square<int>(v1) << endl;
	cout << square<float>(v2) << endl;
	cout << square<double>(v3) << endl;

	cout << square(v1) << endl;
	cout << square(v2) << endl;
}


