#include <stdio.h>
#include "ex22.h"
#include "dbg.h"

int THE_SIZE = 1000;

static int THE_AGE = 37;

int getAge(){
	return THE_AGE;
}

int setAge(int age){
	THE_AGE = age;
}

double updateRatio(double newRatio){
	static double ratio = 1.0;

	double oldRatio = ratio;
	ratio = newRatio;
	
	return oldRatio;
}

void printSize(){
	log_info("Size is: %d", THE_SIZE);
}
