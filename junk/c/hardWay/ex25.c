#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "dbg.h"

#define MAX_DATA 100

int readStr(char **outStr, int maxBuffer){
	*outStr = calloc(1, maxBuffer + 1);
	check_mem(*outStr);
	
	char *result = fgets(*outStr, maxBuffer, stdin);
	check(result != NULL, "Input error");

	return 0;
error:
	if(*outStr) free(*outStr);
	*outStr = NULL;
	return -1;
}

int readInt(int *outInt){
	char *input = NULL;
	int rc = readStr(&input, MAX_DATA);
	check(rc == 0, "Failed to read number");

	*outInt = atoi(input);
	free(input);
	return 0;
error:
	if(input) free(input);
	return -1;
}

int readScan(const char *fmt, ...){
	int i = 0;
	int rc = 0;
	int *outInt = NULL;
	char *outChar = NULL;
	char **outStr = NULL;
	int maxBuffer = 0;

	va_list argp;
	va_start(argp, fmt);

	for(i=0;fmt[i] != '\0';i++){
		if(fmt[i] == '%'){
			i++;
			switch(fmt[i]){
				case '\0':
					sentinel("invalid format");
					break;
				case 'd':
					outInt = va_arg(argp, int *);
					rc = readInt(outInt);
					check(rc == 0, "Failed to read int.");
					break;
				case 'c':
					outChar = va_arg(argp, char *);
					*outChar = fgetc(stdin);
					break;
				case 's':
					maxBuffer = va_arg(argp, int);
					outStr = va_arg(argp, char **);
					rc = readStr(outStr, maxBuffer);
					check(rc == 0, "Failed to read string.");
					break;
				default:
					sentinel("Invalid format");
			}
		}else{
			fgetc(stdin);
		}
		check(!feof(stdin) && !ferror(stdin), "Input error");
	}
	va_end(argp);
	return 0;
error:
	va_end(argp);
	return -1;
}

int main(int argc, char *argv[]){
	char *firstName = NULL;
	char *lastName = NULL;
	char initial = ' ';
	int age = 0;

	printf("First name?");
	int rc = readScan("%s", MAX_DATA, &firstName);
	check(rc == 0, "Failed first name");

	printf("What's your initial? ");
    rc = readScan("%c\n", &initial);
    check(rc == 0, "Failed initial.");

    printf("What's your last name? ");
    rc = readScan("%s", MAX_DATA, &lastName);
    check(rc == 0, "Failed last name.");

    printf("How old are you? ");
    rc = readScan("%d", &age);
	check(rc == 0, "Failed age");

    printf("---- RESULTS ----\n");
    printf("First Name: %s", firstName);
    printf("Initial: '%c'\n", initial);
    printf("Last Name: %s", lastName);
    printf("Age: %d\n", age);

    free(firstName);
    free(lastName);
    return 0;
error:
    return -1;
}
