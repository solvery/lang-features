#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(int argc, char** arg) {
	{
		map<string, int> m;
		m["hello"] = 5;
		cout << m["hello"] << endl;
		m.size();
		map<string,int>::iterator mi;
		for (mi = m.begin(); mi != m.end(); ++mi) {
			cout << mi->first << mi->second << endl;
		}
		m.erase(m.find("hello"));
	}
	{
	}
	{
	}
}


