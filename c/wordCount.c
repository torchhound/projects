#include <stdio.h>
#include <string.h>

void inputProc(int args, char argsArr[]){
	if(args == 0){
		printf("Please enter words, lines, or chars followed by an input or a file");
	}else if(args > 2){
		printf("Too many arguments");
	}
	
	switch(argsArr){
		
	}
}

int words(char input[]){
	int i = 0;
	char *inputPtr = input;
	int words = 0;
	int count = sizeof(input); 
	
	for(i=0;i<=count;i++){
		if(input[i] == 0x20){
			words++;
		}
	}
	return words;
}

int lines(char input[]){
	return 0;
}

int characters(char input[]){
	return 0;
}

int main(int argc, char *argv[]){ //switch/input function?
	printf("Here is the number of words: %d", words(argv);
	
	return 0;
}