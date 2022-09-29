#include <stdio.h>

int main(void)
{
    int senha;
    int r;
    int derrota = 0;

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
        else if (r == senha + 1 || r == senha - 1)
        {
            printf("TÁ QUENTE!");
            derrota++;
        }
        else if (r > senha && r != senha + 1)
        {
            printf("\nO valor digitado é maior que a senha.");
            derrota++;
        }
        else if(r < senha && r != senha - 1)
        {
            printf("\nO valor digitado é menor que a senha.");
            derrota++;
        }

    }

    if (derrota == 5)
        {
            printf("\n\nVocê perdeu! Tente novamente depois.");
        }

    return 0;
}
