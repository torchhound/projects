#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define MAX_DATA 512 //define - cpp constants
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
	FILE *file; //FILE - struct defined by c standard library
	struct database *db;
};

void die(const char *message){
	if(errno){ //errno - external variable for exact error
		perror(message); //perror - print error
	}else{
		printf("ERROR: %s\n",message);
	}
	exit(1);
}

void addressPrint(struct address *addr){
	printf("%d %s %s\n", addr->id, addr->name, addr->email);
}

void databaseLoad(struct connection *conn){
	int rc = fread(conn->db, sizeof(struct database), 1, conn->file); //fread
	if(rc != 1) die("Failed to load database.");
}

struct connection *databaseOpen(const char *filename, char mode){
	struct connection *conn = malloc(sizeof(struct connection));
	if(!conn) die("Memory error");

	conn->db = malloc(sizeof(struct database));
	if(!conn->db) die("Memory error");

	if(mode == 'c'){
		conn->file = fopen(filename, "w"); //fopen
	}else{
		conn->file = fopen(filename, "r+");

		if(conn->file){
			databaseLoad(conn);
		}
	}
	if(!conn->file) die("Failed to open file");
	return conn;
}

void databaseClose(struct connection *conn){
	if(conn){
		if(conn->file) fclose(conn->file);
		if(conn->db) free(conn->db);
		free(conn);
	}
}

void databaseWrite(struct connection *conn){
	rewind(conn->file); //rewind - sets file position of stream to beginning

	int rc = fwrite(conn->db, sizeof(struct database), 1, conn->file); //fwrite
	if(rc != 1) die("Failed to write to database");

	rc = fflush(conn->file);
	if(rc == -1) die("Cannot flush database");
}

void databaseCreate(struct connection *conn){
	int i = 0;

	for(i=0;i<MAX_ROWS;i++){
		struct address addr = {.id = i, .set = 0};
		conn->db->rows[i] = addr;
	}
}

void databaseSet(struct connection *conn, int id, const char *name, const char *email){
	struct address *addr = &conn->db->rows[id];
	if(addr->set) die("Already set");

	addr->set = 1;

	char *res = strncpy(addr->name, name, MAX_DATA); /*strncpy - copies x chars from str pointed to in format <dest> <src> <x>*/

	if(!res) die("Name copy failed");

	res = strncpy(addr->email, email, MAX_DATA);
	if(!res) die("Email copy failed");
}

void databaseGet(struct connection *conn, int id){
	struct address *addr = &conn->db->rows[id];

	if(addr->set){
		addressPrint(addr);
	}else{
		die("ID is not set");
	}
}

void databaseDelete(struct connection *conn, int id){
	struct address addr = {.id = id, .set = 0};
	conn->db->rows[id] = addr;
}

void databaseList(struct connection *conn){
	int i = 0;
	struct database *db = conn->db;

	for(i=0;i<MAX_ROWS;i++){
		struct address *cur = &db->rows[i];
	}
}

int main(int argc, char *argv[]){
	if(argc < 3 || argv[1] == "--help") die("Usage: ex17 <dfile> <action> [action params]");

	char *filename = argv[1];
	char action = argv[2][0];
	struct connection *conn = databaseOpen(filename, action);
	int id = 0;

	if(argc > 3) id = atoi(argv[3]); //atoi - converts str to in
	if(id >= MAX_ROWS) die("Out of bounds");

	switch(action){
		case 'c':
			databaseCreate(conn);
			databaseWrite(conn);
			break;
		case 'g':
			if(argc != 4) die("Need an id");

			databaseGet(conn, id);
			break;
		case 's':
			if(argc != 6) die("Need id, name, and email to set");
			
			databaseSet(conn, id, argv[4], argv[5]);
			databaseWrite(conn);
			break;
		case 'd':
			if(argc != 4) die("Need id to delete");

			databaseDelete(conn, id);
			databaseWrite(conn);
			break;
		case 'l':
			databaseList(conn);
			break;
		default:
			die("Invalid action, valid actions are: g=get, s=set, d=del, l=list");
	}
	databaseClose(conn);
	return 0;
}
