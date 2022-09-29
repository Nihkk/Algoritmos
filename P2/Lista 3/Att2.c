#include <stdio.h>

int fibonacci(int num){

    if(num == 1){
        return 0;
    }

    if(num == 2){
        return 1;
    }

    return fibonacci(num-1) + fibonacci(num-2);
}


int main(void){
    
    int n;

    printf("Digite um numero: ");
    scanf("%d", &n);
    
    printf("O valor da posicao %d eh %d", n,fibonacci(n));

    return 0;
}
