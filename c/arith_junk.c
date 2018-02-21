#include <stdio.h>

int main()
{
  int w, x, y, z;

  w = 0;
  x = 1;
  y = 2;
  z = 3;

  w -= x;
  x += y;
  y *= z;
  z /= w;

  ++w;
  --x;
  w--;
  x++;

  printf("Eat this %d \n %d \n %d \n %d \n.", w, x, y, z);

  return 0;
}
