//protótipo da função, só apresentação.
#include<stdio.h>
#include<stdlib.h>
typedef char obj;
#define max 300
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
int main(void){
	Pilha p1;
	Pilha *p=&p1; 
	int n,b,q,r;
	init(p);
	do{
		printf("Entre com um valor inteiro em DECIMAL para converter \n n >= 1: ");
		scanf("%d",&n);
	}while(n<=0); //Número inteiro Positivo
	do{
		printf("Entre com a base \n 2 <= B <=36: ");
		scanf("%d",&b);
	}while(b<2 && b > 36); //entre 2 e 36
	printf("%d na base %d = [ ",n,b);
	do{
		push(n%b,p);
		n/=b;
	} while ( n ); // Coloca resto da divisão pela base na pilha enquanto n/b != 0
	
	while(!isempty(p)) { //enquanto pilha não acabar
		r = pop(p); // Atribui r ao primeiro elemento da pilha
		if ( r < 10 ) printf("%d",r); // se for possível imprimir valor numérico
		else printf("%c",r+55); // senão for, soma valor com 55 que cai na letra da tabela ASCII (Ex. 10 + 55 = 65, que vale A, em caracter)
		if ((p->topo+1)%4==0) printf(" "); //Para colocar um espaço a cada 4 elementos 
	}
	while(!isempty(p)){
		if(p->topo%4==0) printf("%d ",pop(p)); // separar 4 em 4 dígitos (melhora da visualização em binário)
		else printf("%d",pop(p)); 
	}
	
	puts("]");
	return 0;								  //observar que a exibição será invertida.
}
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
	if(isfull(p)) {printf("!!! stack overflow"); exit(1);} //checa se pilha está cheia;
	else p->s[++p->topo]=x; //atribui a x, o vetor na posição do topo +1
						    //aumenta o indice, e acrescenta um elemento naquela posição;
}
obj pop(Pilha *p){ // 
	if(isempty(p)) {printf("!!! stack underflow");exit(1);} //checa se está vazia, antes de remover.
	else {
		obj x = p->s[p->topo--]; //guarda o topo, e subtrai 1 do indice do topo
		return x; //retorna o valor de x.
	}
}
obj top(Pilha *p){
	if(isempty(p)) printf("!!! stack underflow");
		else
			return p->s[p->topo]; //se não estiver vazia, retorna o elemento do topo;
}