#include <stdio.h>
struct data {
int value;
};
int main()
{
int number;
printf("Please enter a valid integer.");
scanf( "%d", &number );
printf( "You entered %d", number );
struct  data;
return 0;
}