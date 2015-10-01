// copy constructor.
// operator=

#include <iostream>
using namespace std;

class A {
	public:
		A() {
			p = new int(100);
		}
		~A() {
			if(p != NULL) {
				delete p;
				p = NULL;
			}
		}
		A(const A& a) {
			p = new int(*(a.p));
			cout << "copy constructor" << endl;
		}

		A& operator=(const A& a) {
			if(this != &a) {
				if(p != NULL) {
					delete p;
					p = NULL;
				}

				p =new int(*(a.p));
				cout << "operator=" << endl;
			}
		}
	private:
		int *p;     
};

int main() {
	A o1;
	A o2(o1);   
	A o3;
	o3=o1;
	return 0;
}

