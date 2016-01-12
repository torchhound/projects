#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include "object.h"

void objDestroy(void *self){
	object *obj = self;

	if(obj){
		if(obj->description) free(obj->description);
		free(obj);
	}
}

void objDescribe(void *self){
	object *obj = self;
	printf("%s \n", obj->description);
}

int objInit(void *self){
	return 1;
}

void *objMov(void *self, direction direction){
	printf("you can't go that direction");
	return NULL;
}

int objAtk(void *self, int dmg){
	printf("You can't attack that");
	return 0;
}

void *objNew(size_t size, object proto, char *description){
	if(!proto.init) proto.init = objInit;
    if(!proto.describe) proto.describe = objDescribe;
    if(!proto.destroy) proto.destroy = objDestroy;
    if(!proto.attack) proto.atk = objAtk;
    if(!proto.mov) proto.mov = objMov;

	object *el = calloc(1,size);
	*el = proto;

	el->description = strdup(description);

	if(!el->init(e)){
		el->destroy(el);
		return NULL;
	}else{
		return el;
	}
}
