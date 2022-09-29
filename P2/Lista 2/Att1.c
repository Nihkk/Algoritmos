#include <stdio.h>

int main(void)
{
    int val[100];
    int index1, index2, index3, anterior, posterior;

    printf("Digite o valor 1: ");
    scanf("%d", &val[0]);

    int menor = val[0];

    for (int i = 1; i < 100; i++){
        printf("Digite o valor %d: ", i+1);
        scanf("%d", &val[i]);
    }

    printf("\n");

    for (int i = 0; i < 100; i++){
        if (val[i] <= menor){
            menor = val[i];
            anterior = val[i-1];
            posterior = val[i+1];
            index1 = i;
            index2 = i-1;
            index3 = i+1;
        }
    }

    if (index1 == 0){
     printf("Menor valor recebido: %d \n", menor);
     printf("Indice do menor valor: %d \n", index1);
     printf("Valor armazenado na posição posterior [%d]: %d \n", index3, posterior);
    }
    else if (index1 == 2){
     printf("Menor valor recebido: %d \n", menor);
     printf("Indice do menor valor: %d \n", index1);
     printf("Valor armazenado na posição anterior [%d]: %d \n", index2, anterior);
    }
    else
    {
     printf("Menor valor recebido: %d \n", menor);
     printf("Indice do menor valor: %d \n", index1);
     printf("Valor armazenado na posição anterior [%d]: %d \n", index2, anterior);
     printf("Valor armazenado na posição posterior [%d]: %d \n", index3, posterior);
    }

    printf("\n");

    return 0;
}
