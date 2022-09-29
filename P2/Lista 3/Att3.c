#include <stdio.h>

void lerVetor(int vet[]){
    int i = 0;
    while (i < 30){
        int n;
        printf("\nDigite um numero [0 para parar, maximo de 30]: ");
        scanf("%d", &n);

        if(n == 0){
            break;
        }
        else{
            vet[i] = n;
        }

        i++;
    }
}

int buscar(int vet[], int n, int x){
    for (int i = 0; i < n; i++){
        if(vet[i] == x){
            return 1;
        }
    }
    return 0;
}

int main(void){
    
    int val[30], tam, x;

    lerVetor(val);

    printf("\nQuantos numeros foram digitados: ");
    scanf("%d", &tam);

    printf("\nQual numero voce quer buscar: ");
    scanf("%d", &x);

    int r = buscar(val, tam, x);

    if (r == 1){
        printf("\nO numero pertence ao vetor!");
    }
    else{
        printf("\nO numero nao pertence ao vetor!");
    }

    return 0;
}
