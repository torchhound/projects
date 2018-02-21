#include <stdio.h>

int logicAnd(int x, int y) {
	if (x == 1 && y == 1) {
		return 1;
	}
	else {
		return 0;
	}
}

int logicNot(int x) {
	if (x == 1) {
		return 0;
	}
	else {
		return 1;
	}
}

int logicOr(int x, int y) {
	if (x || y == 1) {
		return 1;
	}
	else {
		return 0;
	}
}

int main() {
	int in = 1;
	int alsoIn = 1;
	return logicNot(logicAnd(in, alsoIn));
}
