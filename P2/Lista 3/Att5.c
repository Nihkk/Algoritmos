#include <stdio.h>

void lerVetor(int vet[]){
    for (int i = 0; i < 10; i++)
    {
        printf("Digite o %dº numero: ", i+1);
        scanf("%d", &vet[i]);
    }
}

int somaVetor(int vet[], int tam){
    if (tam == 0){
        return 0;
    }
    else{
       return vet[tam - 1] + somaVetor(vet, tam - 1); 
    } 
}


int main(void){
    
    int nums[10], tam=10;

    lerVetor(nums);
    int soma = somaVetor(nums, tam);

    printf("A soma dos valores do vetor eh: %d", soma);

    return 0;
}
