#include <stdio.h>

void selecao(int a, int b, char vet[][16]){

    printf("\nDigite o primeiro numero: ");
    scanf("%d", &a);
    printf("\nDigite o segundo numero: ");
    scanf("%d", &b);

    int pos = a + b;

    printf("\n%d - %s ", pos, vet[pos]);

}

int main(void){

    int n1, n2;

    char musics[][16] = {"PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!", "CRIPTONIZE", "OFFLINE DAY",
    "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"};

    selecao(n1,n2,musics);

    return 0;
}
