#include <stdio.h>
#include <ctype.h>

int canPrint(char ch);
void printLetters(char arg[]);

void printArgs(int argc, char *argv[]){
	int i = 0;
	
	for(i=0;i<argc;i++){
		printLetters(argv[i]);
	}
}

void printLetters(char arg[]){
	int i = 0;

	for(i=0;arg[i] != '\0';i++){
		char ch = arg[i];

		if(canPrint(ch)){
			printf("'%c' == %d", ch, ch);
		}
	}
	printf("\n");
}

int canPrint(char ch){
	return isalpha(ch) || isblank(ch);
}

int main(int argc, char *argv[]){
	printArgs(argc,argv);
	return 0;
}
