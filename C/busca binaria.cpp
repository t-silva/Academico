#include<stdio.h>
int main(void){
    int v[9]={0,1,2,3,4,5,6,7,8},p=0,u=8,m,x,count=0;
    printf("QUal número deseja procurar?");
    scanf("%d",&x);
    while (p<=u){
    count++;
    m=(p+u)/2;
    printf("%d busca, média = %d\n",count,m);
    if(x==v[m]) return printf("Encontrado, feitas %d buscas",count);
    if (x<v[m]) u = m-1;
    if (x>v[m]) p=m+1;
    }
    return printf("Numero não encontrado, feitas %d buscas",count);
}