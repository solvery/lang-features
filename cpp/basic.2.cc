#include <iostream>
#include <cmath>

using namespace std;

int foo = 7;
extern int bar;

int main(int argc, char** arg) {
	{
		int i;
		int j = 3;
		int k(7);
		const int i1 = 7;
	}

	{
		int n = 1;
		int one = n++;
		int three = ++n;
		int two = --n;
	}
	{
		int i(3);
		int* ip = &i;
		int i2 = *ip + 1;
	}
	{
		cout << sizeof(int) << endl;
		cout << sizeof(int*) << endl;
	}
	{
		int* ip = new int;
		delete ip;
	}
	{
		true;
		false;
	}
	{
		double x1 = pow(2.0, 32.0);
		double x2 = sqrt(2);
		double e = M_E;
		double pi = M_PI;
		double x = 3.7;
		 
		long trnc = static_cast<long>(x);
		long rnd = round(x);
		long flr = floorl(x);
		long cl = ceill(x);
	}
	{
		string s1("lorem ipsum");
		const char* s2 = s1.c_str();
		string* s3 = new string("hello");
		string s4("bar");
		s4[2] = 'z';
	}
	{
		string s("bar");
		string s2 = s;
		string s3(s);
		s[2] = 'z';
	}
	{
		string s1("hello");
		string s2("world");
		int result1 = s1.compare(s2);
		bool result2 = s1 == s2;
		string s("hello");
		string s3 = s + " world";
		s += " world";

		string hbar(80, '-');
	}
	{

		string s("foo");
		// in place:
		transform(s.begin(), s.end(),
				s.begin(), ::toupper);
		transform(s.begin(), s.end(),
				s.begin(), ::tolower);
	}
	{
	}

}


