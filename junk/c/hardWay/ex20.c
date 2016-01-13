#include <stdio.h>
#include <stdlib.h>
#include "dbg.h"

void testDebug(){
	debug("a string");

	debug("look an int, %d", 56);
}

void testLogErr(){
	log_err("everything is kill");
	log_err("There are %d problems in %s.",0,"space");
}

void testLogWarn(){
	log_warn("ignore");
	log_warn("Consider the following %s", "string");
}

void testLogInfo(){
	log_info("nothing to see here");
	log_info("it happened %f times", 1.3f);
}

int testCheck(char *fileName){
	FILE *input = NULL;
	char *block = NULL;

	block = malloc(100);
	check_mem(block);
	
	input = fopen(fileName, "r");
	check(input, "Failed to open %s.", fileName);

	free(block);
	fclose(input);
	return 0;

error:
	if(block) free(block);
	if(input) fclose(input);
	return -1;
}

int testSentinel(int code){
	char *temp = malloc(100);
	check_mem(temp);

	switch(code){
		case 1:
			log_info("It worked.");
			break;
		default:
			sentinel("Ishouldn't run.");
	}

	free(temp);
	return 0;

error:
	if(temp) free(temp);
	return -1;
}

int testCheckMem(){
	char *test = NULL;
	check_mem(test);

	free(test);
	return 1;

error:
	return -1;
}

int testCheckDebug(){
	int i = 0;
	check_debug(i !=0, "Ooops, I was 0.");

	return 0;

error:
	return -1;
}

int main(int argc, char *argv[]){
	check(argc == 2, "Need an argument.");

	testDebug();
	testLogErr();
	testLogWarn();
	testLogInfo();

	check(testCheck("ex20.c") == 0, "failed with ex20.c");
    check(testCheck(argv[1]) == -1, "failed with argv");
    check(testSentinel(1) == 0, "test_sentinel failed.");
    check(testSentinel(100) == -1, "test_sentinel failed.");
    check(testCheckMem() == -1, "test_check_mem failed.");
    check(testCheckDebug() == -1, "test_check_debug failed.");

    return 0;

error:
    return 1;
}
