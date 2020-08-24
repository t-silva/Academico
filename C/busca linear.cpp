#include<stdio.h>
int main(void){
    int v[9]={0,1,2,3,4,5,6,7,8},x;
    printf("QUal número deseja procurar?");
    scanf("%d",&x);
    for (int i=0;i<=8;i++){
        if(x==v[i]) return printf("Número %d encontrado na posição %d\n",x,i);
    }
    return printf("Número não encontrado\n");
}