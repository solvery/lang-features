#include <iostream>

namespace foo {
	namespace bar {
		class Baz {
			public:
			static const int ANSWER = 42;
		};
	}
}

using namespace foo::bar;
using namespace std;

int main(int argc, char** arg) {
	{
		cout << Baz::ANSWER << endl;
	}
}


