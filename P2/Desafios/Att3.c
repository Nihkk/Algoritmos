#include <stdio.h>

void swap(int *x, int *y){
    int troca;
    troca = *x;
    *x = *y;
    *y = troca;
    printf("\nNumeros trocados: a = %d | b = %d \n", *x, *y);
}

int main(void){
    
    int a, b;

    printf("\nDigite o numero 'a': ");
    scanf("%d", &a);
    printf("\nDigite o numero 'b': ");
    scanf("%d", &b);

    printf("\nNumeros em ordem: a = %d | b = %d", a, b);

    swap(&a, &b);

    return 0;
}


