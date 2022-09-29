#include <stdio.h>

int main(void)
{
    int v1, v2, v3;

    printf("Digite um valor: ");
    scanf("%d", &v1);

    printf("Digite um valor: ");
    scanf("%d", &v2);

    printf("Digite um valor: ");
    scanf("%d", &v3);

    if(v1 < v2 && v1 < v3){
        if(v2 < v3){
            printf("%d - %d - %d ", v1, v2, v3);
        }else{
            printf("%d - %d - %d ", v1, v3, v2);
    
        }
    
    
    }else if(v2 < v1 && v2 < v3)
    {
      if(v1 < v3){
            printf("%d - %d - %d ", v2, v1, v3);
        }else{
            printf("%d - %d - %d ", v2, v3, v1);
    
        }
        
    }else if(v3 < v1 && v3 < v2)
    {
      if(v1 < v2){
            printf("%d - %d - %d ", v3, v1, v2);
        }else{
            printf("%d - %d - %d ", v3, v2, v1);
    
        }
    }
    
    
    

 return 0;
}
