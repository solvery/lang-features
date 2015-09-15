#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

void
reverse(int* a, size_t len) {
	for (int i = 0; i < len / 2; ++i) {
		int tmp = a[len - i - 1];
		a[len - i - 1] = a[i];
		a[i] = tmp;
	}
}

int
comp(const void* ap, const void* bp) {
	int a = *(int*)ap;
	int b = *(int*)bp;
	return a < b ? -1 : (a == b ? 0 : 1);
}

int main(int argc, char** arg) {
	{
		int a[10];
		int first = a[0];
		a[0] = 7;
	}
	{
		int* a = new int[10];
		delete[] a;
	}
	{
		int a[] = {1, 2, 3};
		size_t len = sizeof(a) / sizeof(a[0]);
	}
	{
		const size_t LEN(4);
		int src[LEN] = {3, 2, 4, 1};
		int dest[LEN];
		memcpy(dest, src, LEN * sizeof(src[0]));
	}
	{
		const size_t LEN(4);
		int a[LEN] = {3, 2, 4, 1};
		reverse(a, LEN);
	}
	{
		const size_t LEN(4);
		int a[LEN] = {3, 2, 4, 1};

		for (int i = 0; i < LEN; ++i) {
			cout << "value at " << i << " is "
				<< a[i] << endl;
		}
	}
	{
		const size_t LEN(4);
		int a[LEN] = {3, 2, 1, 4};

		qsort(a, LEN, sizeof(a[0]), &comp);
	}
	{
	}
}
