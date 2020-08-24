//protótipo da função, só apresentação.
#include<stdio.h>
#include<stdlib.h>
typedef char obj;
#define max 5
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
	Pilha *p=&p1; //p passa a ser um ponteiro que apontará o endereço da pillha p1
	char letra;
	init(p);
	printf("Vamos testar pilha\n");
	do{
		letra = getchar();fflush(stdin);
		if(letra!='.')push(letra,p);
	} while(letra!='.'); //adiciona até digitar '.'
	while(!isempty(p)) printf("%c\n",pop(p)); //remove o ultimo item, exibindo ele na tela
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