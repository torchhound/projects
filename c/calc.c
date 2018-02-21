/* a simple calculator */
#include <stdio.h>

int add(int x, int y)
{
  int aresult;
  aresult = (x + y);
  return aresult;
}

int subt(int x, int y)
{
  int sresult;
  sresult = (x - y);
  return sresult;
}

int mult(int x, int y)
{
  int mresult;
  mresult = (x * y);
  return mresult;
}

int div(int x, int y)
{
  int dresult;
  dresult = (x / y);
  return dresult;
}

 int main()
 {
   int result;
   result = add(6, 9);
   result = subt(result, 9);
   result = mult(result, 4);
   result = div(result, 5);
   printf("The result is %d.\n",result);
   return 0;
 }
