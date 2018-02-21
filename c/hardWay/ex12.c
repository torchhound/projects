#include <stdio.h>

int main(int argc, char *argv[]){
	int i = 0;

	if(argc == 1){
		printf("1 arg detected\n");
	}else if(argc > 1 && argc < 4){
		printf("Here's your arguments:\n");
		for(i = 1; i < argc; i++){
			printf("%s\n", argv[i]);
		}
	}else{
		printf("Too many args detected, how unfortunate\n");
	}

	return 0;
}
