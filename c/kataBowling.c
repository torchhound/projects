#include <stdio.h>
#include <string.h>

int parse(int count, char *argv[]){
	if(argv[0][count] == 'X'){
		return 10 + argv[1][count + 1] + argv[1][count + 2];
	}else if(argv[0][count] == '/'){
		return 10 + argv[1][count + 1];
	}else{
		return argv[1][count];
	}
}

int main(int argc, char *argv[]){
	int total = 0;
	int count = 0;
	int countArgv = 0;
	int i;

	for(i=0;i<strlen(argv[1]);i++){
		count = count + 1;
		switch(argv[1][countArgv]){
			case 'X':
				total = total + 10 + parse(count, argv) + parse(count + 1, argv);
				//printf("stuff");
				break;
			case '/':
				total = total + 10 + parse(count, argv);
				//printf("stuff");
				break;
			case '-':
				total = total + 0;
				break;
			default:
				total = argv[1][countArgv] + total - '0';
				//printf("total is %d\n", total);
				break;
		}
		countArgv = countArgv + 1;
	}
	printf("Your score is %d\n", total);
	return 0;
}

