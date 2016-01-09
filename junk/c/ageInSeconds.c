#include <stdio.h>

int leap(float x){
	int y, z;
	z = x/4;
	y = (x - z)*365+z*366;
	return y;
}

int main(){
	float input, output;
	printf("Enter age in years: ");
	scanf(%f, &input);
	output = leap(input)*24*60*60
	printf("Your age in seconds is %c", output);
	return 0;
}