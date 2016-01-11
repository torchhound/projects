#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define MAX_DATA 512
#define MAX_ROWS 100

struct address{
	int id;
	int set;
	char name[MAX_DATA];
	char email[MAX_DATA];
};

struct database{
	struct address rows[MAX_ROWS];
};

struct connection{
	FILE *file;
	struct database *db;
};

void die(const char *message){
	if(errno){
		perror(message);
	}else{
		printf("ERROR: %s\n",message);
	}
	exit(1);
}

void addressPrint(struct address *addr){
	printf("%d %s %s\n", addr->id, addr->name, addr->email);
}

void databaseLoad(struct connection *conn){
	int rc = fread(conn->db, sizeof(struct database), 1, conn->file);
	if(rc != 1) die("Failed to load database.");
}
