#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char** arg) {
	{
		vector <int> a;
	}
	{
		vector<int> a = {1, 2, 3};
		vector<int> a2({7, 8, 9});
		size_t len = a.size();

		size_t cap = a.capacity();
		a.reserve(10);
		bool is_empty = a.empty();
		a.clear();
		int n = a[0];
		int n2 = a.at(0);
		a[2] = 4;
	}
	{
		vector<int> a({6, 7, 8, 9});
		auto iter = find(a.cbegin(), a.cend(), 8);
		if (iter != a.cend()) {
			size_t pos = *iter;
		}
	}
	{
		vector<int> a({6, 7, 8, 9});
		vector<int> a2(a.cbegin() + 1,
				a.cbegin() + 3);
	}
	{
		vector<int> a({6, 7, 8, 9});
		vector<int> a2(a.cbegin() + 1, a.cend());
	}
	{
		vector<int> a({6, 7, 8});

		a.push_back(9);
		a.pop_back(); // without return value
	}
	{
		vector<int> a({6, 7, 8});
		//a.insert(a.cbegin(), 5);
		a.insert(a.begin(), 5);
		int elem = a[0];
		a.erase(a.begin());
	}
	{
		vector<int> a1({1, 2, 3});
		vector<int> a2({4, 5, 6});
		a1.insert(a1.cend(), a2.cbegin(), a2.end());
	}
	{
		vector<int> a(10, 0);
	}
	{
		vector<int> a({1, 2, 3});
		//copy constructor:
		vector<int> a2(a);
		vector<int> a3;

		//assignment performs copy:
		a3 = a;
	}
	{
		int sum(0);
		vector<int> a({1, 2, 3});

		for (const auto& n: a) {
			sum += n;
		}
	}
	{
		vector<int> a({6, 7, 8});

		for (auto iter = a.cbegin();
				iter != a.cend();
				++iter) {

			cout<<"value at "<<iter - a.cbegin()
				<<" is "<<*iter<<endl;
		}
	}
	{
		vector<int> a({1, 2, 3});
		vector<int> a2(a.crbegin(), a.crend());
	}
	{
		vector<int> a({3, 2, 4, 1});
		sort(a.begin(), a.end());
	}
	{
	}
	{
	}
	{
	}
	{
	}
}

