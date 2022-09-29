#include <stdio.h>

int main(void)
{
    int mat[4][4];

    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            printf("Digite o valor [%d][%d]: ", i+1, j+1);
            scanf("%d", &mat[i][j]);
        }
    }
    
    printf("\n");

    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
    
    printf("\n");

    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
             printf("%d ", mat[j][i]);
        }
        printf("\n");
    }

    return 0;
}
