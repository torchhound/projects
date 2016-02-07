#include <stdio.h>
#include <time.h>
#include <regex.h>

int getTime(){
	time_t curTime = time(0); // get the system time
	printf(ctime(&curTime));
	return curTime;
}

int main(){
	int i = 0;
	int time = getTime();
	int size = sizeof(time)/sizeof(int);
	regex_t regex;
	int rgx = regcomp(&regex, "[a-zA-Z-\s]", 0); 
	
	for(i=0;i<size;i++){
		reti = regexec(&regex, "[a-zA-Z-\s]", 0, NULL, 0);
        if(reti){
                puts("\t");
        }else if(!reti){
			switch(time){
				case 0:
					printf("---\n|   |\n|   |\n---");
					break;
				case 1:
					printf(" - \n | \n | \n---");
					break;
				case 2:
					printf("---\n  |\n---\n|__");
					break;
				case 3:
					printf("---\n  |\n---\n__|");
					break;
				case 4:
					printf("| |\n---\n  |\n  |");
					break;
				case 5:
					printf("---\n|  \n---\n__|");
					break;
				case 6:
					printf("---\n|   \n---\n|_|");
					break;
				case 7:
					printf("---\n  |\n  |\n  |");
					break;
				case 8:
					printf("---\n| |\n---\n|_|");
					break;
				case 9:
					printf("---\n| |\n---\n  |");
					break;
				default:
						return -1;		
			}
		}
	}
	return 0;
}
