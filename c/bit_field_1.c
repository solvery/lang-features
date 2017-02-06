#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/*
 **Sample code by virHappy
 */

typedef signed int t;
typedef int plain; 

//anoymous member
struct  tag {
    unsigned t:4;
    const t:5;
    plain r:5;
};
// member is char
struct rec {
    unsigned char a:1;
    unsigned char b:1;
    unsigned char c:1;
    unsigned char d:1;
};

// member is unsigned int
struct rec_int {
    unsigned int a:1;
    unsigned int b:1;
    unsigned int c:1;
    unsigned int d:1;
};


#define  TEST_AND_SET_BIT(x) \
    do{                        \
        if ((x)) {             \
            printf("bit alread set.\n"); \
        } else {               \
            (x) = 1;           \
        }                      \
    }while(0)

int main()
{
    struct tag st;
    struct rec sr;

    printf("size of tag is: %d\n", sizeof(st));
    printf("size of rec is: %d\n", sizeof(sr));
    printf("size of rec is: %d\n", sizeof(struct rec_int));
    printf("size of rec is: %d\n", sizeof(int));

    memset(&sr, 0, sizeof(struct rec));
    TEST_AND_SET_BIT(sr.a);
    TEST_AND_SET_BIT(sr.b);
    TEST_AND_SET_BIT(sr.c);
    TEST_AND_SET_BIT(sr.d);

    TEST_AND_SET_BIT(sr.a);
    TEST_AND_SET_BIT(sr.b);
    TEST_AND_SET_BIT(sr.c);
    TEST_AND_SET_BIT(sr.d);
    return 0;
}

