#include <stdio.h>

int main(int argc, char *argv[]){
	int distance = 100;
	float power= 1.234f;
	double superPower = 5467.7894;
	char initial = 'A';
	char firstName[] = "John"; //array of chars
	char lastName[] = "Silver";

	printf("%d miles away\n", distance);
	printf("%f power left\n", power);
	printf("%f amount of super powers\n", superPower);
	printf("%c is an initial\n", initial);
	printf("%s is my first name\n", firstName);
	printf("%s is my last name \n", lastName);
	printf("My whole name is %s %c %s.\n", firstName, initial, lastName);
	return 0;
}
