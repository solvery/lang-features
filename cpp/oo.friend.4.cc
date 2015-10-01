// friend class
// http://www.cplusplus.com/doc/tutorial/inheritance/
#include <iostream>
using namespace std;

class Square;

class Rectangle {
	private:
		int width, height;
	public:
		int area ()
		{return (width * height);}
		void convert (Square a);
};

class Square {
	private:
		friend class Rectangle;
	private:
		int side;
	public:
		Square (int a) : side(a) {}
};

void Rectangle::convert (Square a) {
	width = a.side;
	height = a.side;
}

int main () {
	Rectangle rect;
	Square sqr (4);
	rect.convert(sqr);
	cout << rect.area();
	return 0;
}
