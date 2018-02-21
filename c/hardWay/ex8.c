#include <stdio.h>

int main(int argc, char *argv[]){
	int area[] = {10,12,13,14,20};
	char name[] = "Zed";
	char fullName[] = { 'Z','e', 'd',' ','A','.',' ','S','h','a','w','\0'};
	
	printf("The size of an int: %ld\n", sizeof(int));
	printf("size of area (int[]): %ld\n", sizeof(area));
	printf("number of ints in area: %ld\n", sizeof(area)/sizeof(int));
	printf("The first area is %d, the second %d\n", area[0], area[1]);
	printf("size of char %ld\n", sizeof(char));
	printf("size of name %ld\n", sizeof(name));
	printf("The number of chars %ld\n", sizeof(name)/sizeof(char));
	printf("size of fullName %ld\n", sizeof(fullName));
	printf("The number of chars in fullName: %ld\n", sizeof(fullName)/sizeof(char));
	printf("name = \"%s\" and fullName = \"%s\"\n", name, fullName);
	
	return 0;
}
