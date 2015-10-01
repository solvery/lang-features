#include <typeinfo>
#include <iostream>
#include <string>
#include <vector>
using std::cout;
using std::endl;

int func(int arg){return 0;}
typedef int (*func_ptr)(int arg);

class Base {public: Base(){}};

int main()
{
	int integer(1);
	double real(1.0);
	int array[10]={1,2,3};
	int * array_header = array;
	std::string string;
	std::vector<int> int_vector;
	func_ptr f = func;

	cout<<"integer     : "<<typeid(integer).name()     <<endl;
	cout<<"real        : "<<typeid(real).name()        <<endl;
	cout<<"array[10]   : "<<typeid(array).name()       <<endl;
	cout<<"array_header: "<<typeid(array_header).name()<<endl;
	cout<<"std::string : "<<typeid(string).name()      <<endl;
	cout<<"std::vector : "<<typeid(int_vector).name()  <<endl;
	cout<<"function    : "<<typeid(func).name()        <<endl;
	cout<<"function ptr: "<<typeid(f).name()           <<endl;
	cout<<"custom class: "<<typeid(Base()).name()      <<endl;

	cout<<std::endl;

	cout<<"int         : "<<typeid(int).name()             <<endl;
	cout<<"double      : "<<typeid(double).name()          <<endl;
	cout<<"std::vector : "<<typeid(std::vector<int>).name()<<endl;
	cout<<"Base        : "<<typeid(Base).name()            <<endl;
	cout<<"Base*       : "<<typeid(Base*).name()           <<endl;
	cout<<"Base&       : "<<typeid(Base&).name()           <<endl;

	return 0;
}

