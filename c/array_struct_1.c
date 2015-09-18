
#include <stdio.h>

typedef struct {
	int v1;
	int v2;
}ST;

ST sa[] = {
	{1,2},
	{3,4},
	{5,6},
	{7,8}
};

int main(int argc, char **argv) {
	int i;
	int v1,v2;
	for (i=0; i<(sizeof(sa)/sizeof(ST)); i++) {
		v1 = sa[i].v1;
		v2 = sa[i].v2;
		printf("v1=%d  v2=%d\n", v1, v2);
	}

}

