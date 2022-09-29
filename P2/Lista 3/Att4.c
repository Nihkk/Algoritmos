#include <stdio.h>

void lerMatriz(int m[3][3]){
    int i, j;
    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            printf("\nDigite o valor [%d][%d]: ", i+1, j+1);
            scanf("%d", &m[i][j]);
        }
    }
}

int matrizIdentidade(int m[3][3]){
    int i, j;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if ((i != j && m[i][j] != 0) || (i == j && m[i][j] != 1))
            {
                return 0;
            }
            
        }
        
    }
    return 1;
}

int main(void){

    int mat[3][3];

    lerMatriz(mat);

    int r = matrizIdentidade(mat);

    if (r == 1){
        printf("\nEh uma matriz identidade!");
    }
    else{
        printf("\nNaum eh uma matriz identidade!");
    }

    return 0;
}
