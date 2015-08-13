#include <stdio.h>

extern C {
	#include "lua.h"
	#include "lualib.h"
	#include "luaxlib.h"
}

lua_State* luaObj;

int main() {
	
	luaObj = lua_open();
	if (luaObj == NULL) {
		printf("Internal Lua Error \n Press any key to continue...");
		getchar();
		return -1;
	}
	else {
		luaL_openlibs(luaObj);
		luaL_dofile(luaObj, "practice.lua");
		lua_close(luaObj);
		return 0;
	}
}