#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct person{
	char *name;
	int age;
	int height;
	int weight;
};

struct person *personCreate(char *name, int age, int height, int weight){
	struct person *who = malloc(sizeof(struct person));
	assert(who != NULL);
	who->name = strdup(name);
	who->age = age;
	who->height = height;
	who->weight = weight;
	return who;
}

void personDestroy(struct person *who){
	assert(who != NULL);
	free(who->name);
	free(who);
}

void personPrint(struct person *who){
	printf("");
	printf("");
	printf("");
	printf("");
}
