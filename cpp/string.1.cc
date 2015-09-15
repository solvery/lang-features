#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>

using namespace std;

int main(int argc, char** arg) {
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
		transform(s.begin(), s.end(), s.begin(), ::toupper);
		transform(s.begin(), s.end(), s.begin(), ::tolower);

		string s2;
		s2.resize(s.size());
		transform(s.begin(), s.end(), s2.begin(), ::toupper);

	}
	{
		// trim
		string s(" hello ");
		// trim in place on left:
		s.erase(
				s.begin(),
				find_if(
					s.begin(),
					s.end(),
					not1(ptr_fun<int, int>(isspace))
					)
			   );

		// trim in place on right:
		s.erase(
				find_if(
					s.rbegin(),
					s.rend(),
					not1(ptr_fun<int, int>(isspace))
					).base(),
				s.end()
			   );
	}
	{
		// pad
		string s("hello");
		string rpad(s);
		rpad += string(10 - s.length(), ' ');

		ostringstream oss;
		oss << setw(10) << s;
		string lpad(oss.str());
	}
	{
		// number to string
		char buf[100];
		long n = 123;

		sprintf(buf, "%ld", n);
		/* prevent buffer overflow: */
		snprintf(buf, 100, "%ld", n);
	}
	{
		// string to number 
		stringstream ss("7 14.3 12");
		int n1;
		double x;
		long n2;

		ss >> n1 >> x >> n2;
	}
	{
		string s("hello");
		size_t len = s.length();
		string("hello").find("ll");
		string("hello").substr(2, 2);

	}
	{
		char n = 'X';
		isalpha(n); 
		isdigit(n);
		isspace(n);
		isupper(n);
		islower(n);
	}
	{
	}
}


