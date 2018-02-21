#include <stdio.h>

int main()
{
  char input, input1;
  printf("Please type two characters: \n");
  input = getc(stdin);
  input1 = getchar();
  printf("You typed: %c%c \n", input, input1);
  return 0;
}
  
