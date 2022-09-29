#include <stdio.h>
#include <string.h>

int main(void)
{
    char nomes[2][10][100];
    float notas[2][10][2];

    printf("\n");
    printf("== Atribua o nome e as notas dos alunos de cada turma ==");
    printf("\n\n");

    for (int i = 0; i < 2; i++){
        printf("Turma %d: \n\n", i+1);
        for (int j = 0; j < 10; j++){
            printf("Aluno %d: ", j+1);
            scanf("%s", &nomes[i][j]);
            for (int k = 0; k < 2; k++){
                printf("Nota %d: ", k+1);
                scanf("%f", &notas[i][j][k]);
            }
            printf("\n");
        } 
    }
    
printf("== Boletins ==");
printf("\n\n");

for (int i = 0; i < 2; i++){
        printf("Turma %d: \n\n", i+1);
        for (int j = 0; j < 10; j++){
            printf("%s: \n", nomes[i][j]);
            for (int k = 0; k < 2; k++){
                printf("Nota %d: %.1f", k+1, notas[i][j][k]);
                printf("\n");
            }
            printf("\n");
        } 
    }

    return 0;
}

