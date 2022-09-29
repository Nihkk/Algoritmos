#include <stdio.h>

void swap (int *n1, int *n2){
    int aux;
    aux = *n1;
    *n1 = *n2;
    *n2 = aux;
}

int main(void){
   int a, b;

    printf("Informe um valor: ");
    scanf("%d", &a);
    printf("Informe um valor: ");
    scanf("%d", &b);

    swap(&a, &b);

    printf("Valor de a = %d ---- Valor de b = %d", a,b);

   return 0;
}