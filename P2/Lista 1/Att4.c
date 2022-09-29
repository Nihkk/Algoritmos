#include <stdio.h>

int main(void)
{
    int senha;
    int r;

    printf("\nJogador 1, informe uma senha entre 0 e 100: ");
    scanf("%d", &senha);

    for(int i = 0; i < 5; i++){
        printf("\n\nJogador 2, adivinhe a senha (5 tentativas): ");
        scanf("%d", &r);

        if (r == senha)
        {
            printf("\nVocê acertou a senha!");
            break;
        }
        else if (r > senha)
        {
            printf("\nO valor digitado é maior que a senha.");
        }
        else
        {
            printf("\nO valor digitado é menor que a senha.");
        }

    }

    return 0;
}
