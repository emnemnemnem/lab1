#include <stdlib.h>
#include <stdio.h>

int main () {
	#define LEN 32 // 256 bits
	unsigned char *key = (unsigned char *) malloc(sizeof(unsigned char)*LEN);
	FILE* random_nums = fopen("/dev/urandom", "r");
	fread(key, sizeof(unsigned char)*LEN, 1, random_nums); 

	for(int i = 0; i < LEN; i++) {
 		printf("%.2x", key[i]);
	}
	printf("\n");
	fclose(random_nums);
	return (0);
}