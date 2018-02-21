#include <stdio.h>

int main(int argc, char *argv[]){
	int bugs = 100;
	double bugRate = 1.2;
	
	printf("%d bugs at a rate of %d\n", bugs, bugRate);
	
	long universeOfDefects = 1l*1024L*1024L*1024L;
	printf("The entire universe has %ld bugs.\n", universeOfDefects);

	double expectedBugs = bugs*bugRate;
	printf("You can expect %f bugs.\n",expectedBugs);

	double partOfUniverse = expectedBugs/universeOfDefects;
	printf("That is only a %e portion of the universe.\n", partOfUniverse);

	char nullByte = '\0';
	int carePercentage = bugs*nullByte;
	printf("Which means you should care %d%%.\n", carePercentage);

	return 0;
}
