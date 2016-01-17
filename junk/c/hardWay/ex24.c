#include <stdio.h>
#include "dbg.h"

#define MAX_DATA 100

typedef enum eyeColor{
	BLUE_EYES, GREEN_EYES, BROWN_EYES,
    BLACK_EYES, OTHER_EYES
} eyeColor;

const char *EYE_COLOR_NAMES[] = {
	"Blue", "Green", "Brown", "Black", "Other"
};

typedef struct person {
	int age;
	char firstName[MAX_DATA];
	char lastName[MAX_DATA];
	eyeColor eyes;
	float income;
} person;

int main(int argc, char *argv[]){
	person you = {.age = 0};
	int i = 0;
	char *in = NULL;

	printf("Enter 1st name: ");
	in = fgets(you.firstName, MAX_DATA-1, stdin);
	check(in != NULL, "Failed to read 1st name.");

	printf("What's your last name? ");
    in = fgets(you.lastName, MAX_DATA-1, stdin);
    check(in != NULL, "Failed to read last name.");

    printf("How old are you? ");
    int rc = fscanf(stdin, "%d", &you.age);
    check(rc > 0, "You have to enter a number.");

	printf("What is your eye color:\n");
	for(i=0;i<=OTHER_EYES;i++){
		printf("%d) %s\n", i+1, EYE_COLOR_NAMES[i]);
	}
	printf("> ");

	int eyes = -1;
	rc = fscanf(stdin, "%d", &eyes);
	check(rc > 0, "You have to enter a number.");

	you.eyes = eyes - 1;
	check(you.eyes <= OTHER_EYES && you.eyes >= 0, "Not an option");

	printf("income?");
	rc = fscanf(stdin, "%f", &you.income);
	check(rc > 0, "Please enter a valid number.");

	printf("--RESULTS--");

	printf("First Name: %s", you.firstName);
    printf("Last Name: %s", you.lastName);
    printf("Age: %d\n", you.age);
    printf("Eyes: %s\n", EYE_COLOR_NAMES[you.eyes]);
    printf("Income: %f\n", you.income);

    return 0;
error:

    return -1;
}
