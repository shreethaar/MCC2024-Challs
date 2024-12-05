#include <stdio.h>

int main() {
	int sum = 0x45BEB206;
	sum ^= 0x0BA14C823;
	sum -= 0x0D1507BA;
	sum ^= 0x0AAFBBCBE;
	sum -= 0x45370DF7;
	printf("%x", sum);
	return 0;
}
