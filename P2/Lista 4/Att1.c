#include <stdio.h>

int main(void){
   int x = 2, y= 8, *p, *q;

   p = &x;
   q = &y;

   printf("\nEndereço de x: %p -- Valor de x: %d", &x, x);
   printf("\nValor de p: %p -- Valor de *p: %d", p, *p);
   printf("\nEndereço de y: %p -- Valor de y: %d", &y, y);
   printf("\nValor de q: %p -- Valor de *q: %d", q, *q);    


   return 0;
}
