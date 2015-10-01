#include <stdio.h>
#include <stdint.h>

#define FORMAT(T, DESC) "%-8s\t%-6lu\t%s\n"
#define PRINT_SIZE_OF(T, DESC) printf(FORMAT(T, DESC), #T, (unsigned long)sizeof(T), DESC)

class A1 { };
class A2 { char c; };
class A3 { public: void foo(){} };
class A4 { public: virtual void foo(){} };
class A5 { public: virtual void foo()=0;};
class B1 : public A1 { };
class B2 : public A1 { char c; };
class B3 : virtual public A1 { };
class B4 : virtual public A2 { };

int main(int argc, char** arg) {

    printf("/%-8s\t/%-6s\t/%s\n\n", "type", "bytes", "desc");

	PRINT_SIZE_OF(int*, "");
	PRINT_SIZE_OF(long*, "");
	PRINT_SIZE_OF(char*, "");
	PRINT_SIZE_OF(float*, "");
	PRINT_SIZE_OF(A1, "class A1 { };                             ");
	PRINT_SIZE_OF(A2, "class A2 { char c; };                     ");
	PRINT_SIZE_OF(A3, "class A3 { public: void foo(){} };        ");
	PRINT_SIZE_OF(A4, "class A4 { public: virtual void foo(){} };");
	PRINT_SIZE_OF(A5, "class A5 { public: virtual void foo()=0;};");
	PRINT_SIZE_OF(B1, "class B1 : public A1 { };                 ");
	PRINT_SIZE_OF(B2, "class B2 : public A1 { char c; };         ");
	PRINT_SIZE_OF(B3, "class B3 : virtual public A1 { };         ");
	PRINT_SIZE_OF(B4, "class B4 : virtual public A2 { };         ");
}

