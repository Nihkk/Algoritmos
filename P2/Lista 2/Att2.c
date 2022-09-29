#include <stdio.h>
#include<stdlib.h>

int main(void)
{
   int sub, i, j;
   int vet[100];

   for (i = 0; i < 100; i++){  
       printf("\nDigite o valor %d: ", i+1);
       scanf("%d", &vet[i]);
   }

   for (i = 0; i < 100; i++){
       for (j = i; j < 100; j++){
           if (vet[j] < vet[i]){
               sub = vet[i];
               vet[i] = vet[j];
               vet[j] = sub;
           }  
       }
   }

   printf("\nNúmeros em ordem crescente: \n");
   
   for (i = 0; i < 100; i++){
       printf("\n%d", vet[i]);
   }
   
    return 0;
}
