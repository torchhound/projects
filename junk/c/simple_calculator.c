#include <studio.h>
#include <math.h>
int main() /*int or void?*/
{
printf(" Simple Calculator v1.0\n Calculator can only calculate addition, subtraction, multiplication, and division.\n Enter number of digits in calculation.\n  ");
int digits;
int number[digits] = {};
scanf(%d, &digits);
for (i=0,i<=%d,i++,&digits) /* i<=digits or at the end stop when i == digits?*/
{
	printf("Enter digit:");
	scanf(%d, &number);
	}
printf("Please enter desired calculation method.\n Note: currently only one type +, -, *, or / can be used at a time.\n");
char method;
scanf(%c, method);
printf("You have selected %c also known as %d\n, method, method");
for (i=0,i<=%d,i++,number) /*number or size of array?*/
{
	int result = number method; /*transform method*/
}
return result /*return result or printf result also does returning a variable that is an int count as returning an int */
}