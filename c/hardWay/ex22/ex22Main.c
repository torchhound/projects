#include "ex22.h"
#include "dbg.h"

const char *MY_NAME = "J Random Hacker";

void scopeDemo(int count){
	log_info("count is: %d", count);

	if(count>10){
		int count = 100;

		log_info("count in this scope is %d", count);
	}

	log_info("At exit count is: %d", count);

	count = 300;

	log_info("count after assign: %d", count);
}

int main(int argc, char *argv[]){
	log_info("My name is %s, and my age is %d", MY_NAME, getAge());

	setAge(100);

	log_info("My new age is %d", getAge());

	log_info("THE_SIZE is %d", THE_SIZE);
	printSize();

	THE_SIZE = 9;

	log_info("THE SIZE is now %d", THE_SIZE);
    printSize();

	log_info("1st ratio %f", updateRatio(2.0));
	log_info("2nd ratio %f", updateRatio(10.0));
	log_info("3rd ratio %f", updateRatio(300.0));

	int count = 4;
	scopeDemo(count);
	scopeDemo(count * 20);

	log_info("count after calling scopeDemo %d", count);

	return 0;
}
