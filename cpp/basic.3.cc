#include <iostream>

using namespace std;

int main(int argc, char** arg) {
	int n = 0;
	int m = 0;
	{
		int signum;

		if (n > 0) {
			signum = 1;
		}
		else if (n == 0) {
			signum = 0;
		}
		else {
			signum = -1;
		}
	}
	{
		if (n == 0)
			if (m == 0)
				cout << "n and m are zero" << endl;
			else
				cout << "n is zero; m isn't" << endl;
	}
	{
		const int INVALID_BINARY_DIGIT(-1);
		int bin_digit;

		switch(n) {
			case 0:
			case 1:
				bin_digit = n;
				break;
			default:
				bin_digit = INVALID_BINARY_DIGIT;
				break;
		}
	}
	{
		int i(1), fact(1), n(10);

		while (i < n) {
			fact *= i;
			++i;
		}
	}
	{
		int fact, n(10);

		for (int i = 1, fact = 1; i <= n; ++i) {
			fact *= i;
		}
	}
	{
		int data[4] = {3, 2, 0, 1};
		int i;
		bool has_zero(false);

		for (i = 0; i < 4; ++i) {
			if (data[i] == 0) {
				has_zero = true;
				break;
			}
		}
	}
	{
		int data[2][2] = {{3, 2}, {0, 1}};
		int i, j;
		bool has_zero(false);

		for (i = 0; i < 2; ++i) {
			for (j = 0; j < 2; ++j) {
				if (data[i][j] == 0) {
					has_zero = true;
					goto end_of_loops;
				}
			}
		}
end_of_loops: ;
	}
	{
		int a[4] = {3, 2, 0, 1};

		for (int i = 0; i < 4; ++i) {
			if (a[i] == 0) {
				continue;
			}
			cout << 1.0 / a[i] << endl;
		}
	}
	{
	}
}
