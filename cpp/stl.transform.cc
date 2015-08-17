#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	string s="hello";
	string out;
	transform(s.begin(), s.end(), back_inserter(out), ::toupper);
	cout << out << endl;
}

// 输出：HELLO
// 
