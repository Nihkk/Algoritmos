#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){

    int num, random;

    printf("Digite um valor: ");
    scanf("%d", &num);

    srand(time(NULL));
    random = rand() % 10;

    while(num != random && num != 0){
        printf("Digite um valor: ");
        scanf("%d", &num);
        random = rand() % 3;
    }

    if (num == random && num != 0){
        printf("Acertou! \n");
    }else{
        printf("Saiu \n");
    }

    return 0;
}