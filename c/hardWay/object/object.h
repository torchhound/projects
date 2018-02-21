#ifndef _object_h
#define _object_h

typdef enum {
	NORTH, SOUTH, EAST, WEST
} direction;

typedef struct {
	char *description;
	int (*init)(void *self);
	void (*describe)(void *self);
	void(*destroy)(void *self);
	void *(*mov)(void *self, direction direction);
	int (*atk)(void *self, int dmg);
} object;

int objInit(void *self);
void objDestroy(void *self);
void objDescribe(void *self); 
void *objMov(void *self, direction direction);
int objAtk(void *self, int dmg);
void *objNew(size_t size, object proto, char *description);

#define NEW(T, N) objNew(sizeof(T), T##Proto, N)
#define _(N) proto.N

#endif
