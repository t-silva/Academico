#include<stdio.h>
int main(void){
	int p,q,aux=0;
	scanf("%d",&p);
	scanf("%d",&q);
	do{
		p-=q;
		aux++;
	}while(p>=q);
	printf("%d e R(%d)",aux,p);
return 0;}
