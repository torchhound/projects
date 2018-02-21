#import <stdio.h>
#import <stdbool.h>

bool nand(int a, int b){
	if (a && b == 1){
		return false;
	}else{
		return true;
	}
}