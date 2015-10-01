#include <iostream>
using namespace std;

class A {
	public:
		A()      {
			count++;
		}
		~A()     {
			count--;
		}
		static int getCount()       {
			return count;
		}
	private:
		static int count;       
};

int A::count = 0;        

int main() {
	A o1;
	cout<<"The count of A: "<<A::getCount()<<endl;

	A o2(o1);   
	cout<<"The count of A: "<<A::getCount()<<endl;

	return 0;
}
