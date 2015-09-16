#include <iostream>
#include <exception>
#include <stdexcept>
#include <system_error>
#include <typeinfo>

using namespace std;

void risky() {
	if (1 < 10) {
		throw runtime_error("bam!");
	}
}

class Bam : public runtime_error {
	public:
		Bam() : runtime_error("bam!") {}
};


int main(int argc, char** arg) {
	{
		try {
			risky();
		}
		catch (const exception &e) {
			cout << e.what() << endl;
		}
	}
	{
		try {
			risky();
		}
		catch (const exception& e) {
			cout << "an error occurred..." << endl;
			//throw;
		}
	}
	{
		//throw Bam();
	}
	{
		try {
			risky();
		}
		catch (const system_error &e) {
			cout << "system error: " << e.code()
				<< endl;
		}
		catch (const exception &e) {
			cout << "exception: " << e.what()
				<< endl;
		}
		catch (...) {
			cout << "unknown error" << endl;
		}
	}
	{
		try {
			risky();
		}
		catch (...) {
			cout << "an error was ignored"
				<< endl;
		}
	}
}


