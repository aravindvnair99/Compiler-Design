#include <stdio.h>

void main() {
	int a;
	int b = 10;
	for (a = 0; a <= 10; a++) {
		b += a;
	}
	printf("Final number is %d\n", b);
}
