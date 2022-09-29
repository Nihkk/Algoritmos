int main(void)
{
    float p1, p2, p3;
    float media1, media2;
    float maior;

    printf("\nPrimeira nota: ");
    scanf("%f", &p1);

    printf("\nSegunda nota: ");
    scanf("%f", &p2);

    if (p1 > p2)
    {
        maior = p1;
    }
    else
    {
        maior = p2;
    }
    
    media1 = (p1 + p2)/2;

    if (media1 >= 5.0 && p1 > 3.0 && p2 > 3.0)
    {
        printf("Aprovado!");
    }
    else
    {
        printf("\nTerceira nota: ");
    scanf("%f", &p3);

    media2 = (p3 + maior)/2;

    if (media2 >= 5)
    {
        printf("Aprovado!");
    }
    else
    {
        printf("Reprovado!");
    }
    
    
    }
    


    return 0;
}
