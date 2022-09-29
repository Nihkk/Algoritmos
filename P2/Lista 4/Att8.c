#include <stdio.h>

int main(void){
   int a = 25; 
   int *pa = &a; 
   int b = *pa + a; 
   printf("%d \n%p \n%p \n%d \n%d \n%p\n", a, pa, &a, *pa, b, &b);


   return 0;
}