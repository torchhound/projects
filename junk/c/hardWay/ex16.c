#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct person{ //user defined memory block containing various data types
	char *name;
	int age;
	int height;
	int weight;
};

struct person *personCreate(char *name, int age, int height, int weight){ /*pointer function to struct, pass in args to init struct*/
	struct person *who = malloc(sizeof(struct person)); //pointer to struct's memory address
	assert(who != NULL); //checks if the pointer is null if so it terminates the program
	who->name = strdup(name); //duplicates str with a null char at the end
	who->age = age; //assignment of args to vars
	who->height = height;
	who->weight = weight;
	return who;
}

void personDestroy(struct person *who){ //function that clears memory taken up by struct
	assert(who != NULL);
	free(who->name);
	free(who);
}

void personPrint(struct person *who){ //prints information from struct
	printf("Name: %s\n", who->name);
	printf("\tAge: %d\n", who->age); // backslash t produces a tab char
	printf("\tHeight: %d\n", who->height);
	printf("\tWeight: %d\n", who->weight);
}

int main(int argc, char *argv[]){
	struct person *joe = personCreate("Joe Smith", 32,64,140); /*create a new person and fill the struct with info*/
	struct person *frank = personCreate("Frank the Tank", 20,72,180);

	printf("Joe is at memory location: %p\n", joe); //pointer to mem location
	personPrint(joe); //func print of struct info

	printf("Frank is at memory location: %p\n", frank);
	personPrint(frank);

	joe->age+=20; //reassigns value in struct
	joe->height-=2;
	joe->weight+=40;
	personPrint(joe);

	frank->age+=20;
	frank->weight+=20;
	personPrint(frank);

	personDestroy(joe); //cleans up memory
	personDestroy(frank);

	return 0;
}
