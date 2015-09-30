#include <iostream>

using namespace std;

class A {
	public:
		int v1;
	protected:
		int v2;
	private:
		int v3;

	public:
		A(){
			v1=1;
			v2=2;
			v3=3;
		}
};

class B1 : public A {
	public:
		void b1m1() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
	protected:
		void b1m2() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
	private:
		void b1m3() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
};

class B2 : protected A {
	public:
		void b1m1() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
	protected:
		void b1m2() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
	private:
		void b1m3() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
};

class B3 : private A {
	public:
		void b1m1() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
	protected:
		void b1m2() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
	private:
		void b1m3() {
			A::v1 = 1;
			A::v2 = 2;
			/// A::v3 = 3;
		}
};

int main(int argc, char** arg) {
	{
	}
}



