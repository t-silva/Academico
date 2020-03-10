#include<stdio.h>
#define max 30
typedef struct{
	int topo;
	int s[max];
}Pilha;
void bin(int n){
	Pilha p1;
	Pilha *p=&p1;
	p->topo=-1; //equivalente a init(p);
	do{
		p->s[++p->topo]=n%2;
		n/=2;
		printf("%d\n",n);
	}while(n); //enquanto n/2 for diferente de 0 (divisão por inteiro, 1/2 = 0)
	int i = 0;
	while(p->topo!=-1){ // equivalente a While != isempty;
		int x = p->s[p->topo--]; //equivalente ao pop(p). 
		printf("%d",x); 
	}
	puts("");
}
int main(void){
	int num;
	scanf("%d",&num);
	bin(num);
	return 0;
}
//teste