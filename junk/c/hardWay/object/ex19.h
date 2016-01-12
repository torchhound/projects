#ifndef _ex19_h
#define _ex19_h

#include "object.h"

struct monster{
	object proto;
	int hitPoints;
};

typedef struct monster monster;

int monsterAtk(void *self, int dmg);
int monsterInit(void *self);

struct room{
	object proto;

	monster *badGuy;

	struct room *north;
	struct room *south;
	struct room *east;
	struct room *west;
};

typedef struct room room;

void *roomMov(void *self, direction direction);
int roomAtk(void *self, int dmg);
int roomInit(void *self);

struct map{
	object proto;
	room *start;
	room *location;
};

typedef struct map map;

void *mapMov(void *self, direction direction);
int mapAtk(void *self, int dmg);
int mapInit(void *self);

#endif
