#include <stdio.h>

int main(void){
   int x = 10, *px;

   px = &x;

   int div = *px / 5;

   printf("Divisao: %d", div);

   return 0;
}