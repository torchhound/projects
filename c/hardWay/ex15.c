#include <stdio.h>

int main(int argc, char *argv[]){
	int ages[] = {23,43,12,89,2};
	char *names[] = {"Alan","Frank","Mary","John","Lisa"};
	
	int count = sizeof(ages)/sizeof(int);
	int i = 0;
	
	for(i=0;i<count;i++){
		printf("%s has %d years alive.\n", names[i], ages[i]);
	}

	printf("---\n");

	int *curAge = ages;
	char **curName = names;

	for(i=0;i<count;i++){
		printf("%s is %d years old.\n", *(curName+i), *(curAge+i));
	}

	printf("---\n");

	for(i=0;i<count;i++){
		printf("%s is %d years old.\n", curName[i], curAge[i]);
	}

	printf("---\n");

	for(curName = names, curAge = ages;(curAge - ages) < count;curName++, curAge++){
        printf("%s lived %d years so far.\n",
                *curName, *curAge);
    }

	return 0;
}
