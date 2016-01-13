#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "ex19.h"

int monsterAtk(void *self, int dmg){
	monster *monster = self;

	printf("You attack %s!\n", monster->_(description));

	monster->hitPoints -= dmg;

	if(monster->hitPoints > 0){
		printf("It is still alive.\n");
	}else{
		printf("You have slain %s!\n", monster->description);
		return 1;
	}
}

int monsterInit(void *self){
	monster *monster = self;
	monster->hitPoints = 10;
	return 1;
}

object monsterProto = {
	.init = monsterInit,
	.atk = monsterAtk
};

void *roomMov(void *self, direction direction){
	room *room = self;
	room *next = NULL;

	if(direction == NORTH && room->north){
		printf("You head north, into\n");
		next = room->north;
	}else if(direction == SOUTH && room->south){
		printf("You head south, into:\n");
		next = room->south;
	}else if(direction == EAST && room->east){
		printf("You head east, into:\n");
		next = room->east;
	}else if(direction == WEST && room->west){
		printf("You head west, into:\n");
		next = room->west;
	}else{
		printf("You can't go that way.\n");
		next = NULL;
	}

	if(next){
		next->_(describe)(next);
	}

	return next;
}

int roomAtk(void *self, int dmg){
	room *room = self;
	monster *monster = room->badGuy;

	if(monster){
		monster->(atk)(monster, dmg));
		return 1;
	}else{
		printf("You flail at nothing, good work.\n");
		return 0;
	}
}

object roomPorto = {
	.mov = roomMov,
	.atk = roomAtk
};

void *mapMov(void *self, direction direction){
	map *map = self;
	room *location = map->location;
	room *next = NULL;

	next = location->_(mov)(location, direction);

	if(next){
		map->location = next;
	}

	return next;
}

int mapAtk(void *self, int dmg){
	map* map = self; //typo?
	room *location = map->location;

	return location->_(atk)(location, dmg);
}

int mapInit(void *self){
	map *map = self;

	room *hall = NEW(room, "The great hall");
	room *throne = NEW(room, "The throne room");
	room *armory = NEW(room, "The royal armory");
	room *kitchen = NEW(room, "The kitchen");
	room *arena = NEW(room, "Minotaur zone");

	arena->badGuy = NEW(monster, "The evil minotaur");

	hall->north = throne;
	throne->west = arena;
	throne->east = kitchen;
	throne->south = hall;
	throne->north = armory;
	armory->south = throne;
	arena->east = throne;
	kitchen->west = throne;

	map->start = hall;
	map->location = hall;

	return 1;
}

object mapProto = {
	.init = mapInit,
	.mov = mapMov,
	.atk = mapAtk
};

int processInput(map *game){
	printf("\n> ");

	char ch = getchar();
	getchar(); //gets rid of enter keystroke

	int dmg = rand() % 4;

	switch (ch){
		case -1:
			printf("Only a coward retreats.\n");
			return 0;
			break;
		case 'n':
			game->_(mov)(game, NORTH);
            break;

        case 's':
            game->_(mov)(game, SOUTH);
            break;

        case 'e':
            game->_(mov)(game, EAST);
            break;

        case 'w':
            game->_(mov)(game, WEST);
            break;

        case 'a':

            game->_(atk)(game, dmg);
            break;
        case 'l':
            printf("You can go:\n");
            if(game->location->north) printf("NORTH\n");
            if(game->location->south) printf("SOUTH\n");
            if(game->location->east) printf("EAST\n");
            if(game->location->west) printf("WEST\n");
            break;

        default:
            printf("Huh?: %d\n", ch);
	}

	return 1;
}

int main(int argc, char *argv[]){
	srand(time(NULL));

	map *game = NEW(map, "The Castle of the Minotaur");

	printf("You enter the ");
	game->location->_(descibe)(game->location);

	while(processInput(game)){}

	return 0;
}
