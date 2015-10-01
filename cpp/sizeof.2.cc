#include <stdio.h>
#include <stdint.h>

#define FORMAT(T, DESC) "%-8s\t%-6lu\t%s\n"
#define PRINT_SIZE_OF(T, DESC) printf(FORMAT(T, DESC), #T, (unsigned long)sizeof(T), DESC)

class A
{
};

class B : virtual public A
{
	int a;
};
int main(int argc, char** arg) {

	PRINT_SIZE_OF(A, "");
	PRINT_SIZE_OF(B, "");
}

