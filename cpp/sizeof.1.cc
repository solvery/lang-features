#include <stdio.h>
#include <stdint.h>

#define FORMAT(T, DESC) "%-8s\t%-6lu\t%s\n"
#define PRINT_SIZE_OF(T, DESC) printf(FORMAT(T, DESC), #T, (unsigned long)sizeof(T), DESC)

int main(void)
{
    printf("/%-8s\t/%-6s\t/%s\n\n", "type", "bytes", "desc");

    PRINT_SIZE_OF(size_t, "integral data type");

    printf("\n");

    PRINT_SIZE_OF(char, "one character");
    
    printf("\n");
    
    PRINT_SIZE_OF(int8_t, "standard int 8");
    PRINT_SIZE_OF(int16_t, "standard int 16");
    PRINT_SIZE_OF(int32_t, "standard int 32");
    PRINT_SIZE_OF(int64_t, "standard int 64");

    printf("\n");

    PRINT_SIZE_OF(short, "small integer");
    PRINT_SIZE_OF(int, "integer");
    PRINT_SIZE_OF(long, "big integer");

    printf("\n");

    PRINT_SIZE_OF(float, "floating-point number");
    PRINT_SIZE_OF(double, "double-precision floating-point number");
    PRINT_SIZE_OF(long double, "double-double-precision floating-point number");

    return 0;
}
