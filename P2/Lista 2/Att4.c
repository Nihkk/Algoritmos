#include <stdio.h>

int main(void)
{
    int mat[10][3];
    int num = 0;
    int impar = 0;
    int par = 0;
    int meio = 0;

    while (num!=-1){
        printf("Informe um valor: ");
        scanf("%d", &num);

        if (num %2 != 0 && num != -1){
            if (impar < 10){
                mat[impar][0] = num;
                impar++;
            }
            else if (meio < 10){
                mat[meio][1] = num;
                meio++;
            }
            else{
                for (int i = 0; i < 9; i++){
                    mat[i][1] = mat[i + 1][1]; 
                }
                
                mat[9][1] = mat[0][0];

                for (int i = 0; i < 9; i++){
                    mat[i][0] = mat[i + 1][0]; 
                }

                mat[9][0] = num;
            }
            
            
            
            
        }
        else if(num % 2 == 0 && num != -1){
            if (par < 10){
                mat[par][2] = num;
                par++;
            }
            else if (meio < 10){
                mat[meio][1] = num;
                meio++;
            }
            else{
                for (int i = 0; i < 9; i++){
                    mat[i][1] = mat[i + 1][1]; 
                }
                
                mat[9][1] = mat[0][2];

                for (int i = 0; i < 9; i++){
                    mat[i][2] = mat[i + 1][2]; 
                }

                mat[9][2] = num;
            }
        }  
        
    }

    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 3; j++){
            if (impar<10){
                mat[impar][0] = 0;
                impar ++;
            }
            if (par<10){
                mat[par][2] = 0;
                par ++;
            }
            if (meio<10){
                mat[meio][1] = 0;
                meio ++;
            }
            
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}
