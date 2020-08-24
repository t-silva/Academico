//protótipo da função, só apresentação.
#include<stdio.h>
#include<stdlib.h>
typedef int obj;
#define max 20
typedef struct{ //cria um struct com dois campos, TOPO (controla pilha) e s[max] vetor da pilha.
	int topo; 
	obj s[max];
}Pilha;
// Fim da apresentação
void init( Pilha *p); 
int isempty( Pilha *p);
int isfull( Pilha *p);
void push( obj x,Pilha *p);
obj pop( Pilha *p);
obj top ( Pilha *p);
void init(Pilha *p){
	p->topo=-1; //coloca na controladora de pilha, o valor -1. (anterior ao primeiro elemento '0'
				// quando pensamos em vetores.
}
int isempty(Pilha *p){
	return p->topo==-1; //retorna 1 se topo = -1. (indicando pilha "vazia")
}
int isfull(Pilha *p){
	return p->topo==max-1; //se max-1 (primeiro elemento do vetor está no 0) = topo, retorna 1.
}
void push(obj x, Pilha *p){
	if(isfull(p)) {printf("!!! stack overflow\n"); exit(1);} //checa se pilha está cheia;
	else p->s[++p->topo]=x; //atribui a x, o vetor na posição do topo +1
						    //aumenta o indice, e acrescenta um elemento naquela posição;
}
obj pop(Pilha *p){ // 
	if(isempty(p)) {printf("!!! stack underflow\n");exit(1);} //checa se está vazia, antes de remover.
	else {
		obj x = p->s[p->topo--]; //guarda o topo, e subtrai 1 do indice do topo
		return x; //retorna o valor de x.
	}
}
obj top(Pilha *p){
	if(isempty(p)) printf("!!! stack underflow\b");
		else
			return p->s[p->topo]; //se não estiver vazia, retorna o elemento do topo;
}
void elementos(Pilha *p){
	Pilha v1; //Cria uma pilha de backup.
	Pilha *v = &v1;
	int count=0;
	init(v);
	while (!isempty(p)){ //Copia os elementos para essa nova pilha, 
		push(pop(p),v);
		count++; //contanto a quantidade
	}
	printf("%d elementos na pilha\n",count); //exibe a quantidade
	while (!isempty(v)) push(pop(v),p); //retoma a pilha original
	while(!isempty(p)){ //exibe pilha P para checar 
		if(p->topo%4==0) printf("%d ",pop(p)); // separar 4 em 4 dígitos (melhora da visualização em binário)
		else printf("%d",pop(p)); 
	}
	puts("");
}
void bin(int n, Pilha *p){ 
	//printf("Binario de %d: ",n);
	do{
		push(n%2,p);
		n/=2;
	}while(n); //enquanto n/2 for diferente de 0 (divisão por inteiro, 1/2 = 0)
	elementos(p);
}
int main(void){
	Pilha p1;
	Pilha *p=&p1;
	int num;
	init(p);
	printf("Digite número decimal: ");
	scanf("%d",&num);
	bin(num,p);
	return 0;
}