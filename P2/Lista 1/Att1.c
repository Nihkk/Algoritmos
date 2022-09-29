int main(void)
{
    float a, b, res;

    int oper;

    printf("\n Digite o 1º valor: ");
    scanf("%f", &a);

    printf("\n Digite o 2º valor: ");
    scanf("%f", &b);

    printf("\n Escolha entre: Adição(1) - Subtração (2) - Divisão (3) - Multiplicação (4): ");
    scanf("%d", &oper);

    switch (oper)
    {
    case 1:
        res = a+b;
        printf("\n Resultado = %.1f", res);
        break;
    case 2:
        res = a-b;
        printf("\n Resultado = %.1f", res);
        break;
    case 3:
        res = a/b;
        printf("\n Resultado = %.1f", res);
        break;
    case 4:
        res = a*b;
        printf("\n Resultado = %.1f", res);
        break;
    default:
        printf("Operação inválida");
        break;
    }

    return 0;
}
