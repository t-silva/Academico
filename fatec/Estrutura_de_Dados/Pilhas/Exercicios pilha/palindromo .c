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
int main(void)
{
  Pilha p1;
  Pilha *p=&p1;
  init(p);
  char nome[61];
  printf("Digite seu nome: ");
  scanf("%s",nome);
  int i=0, resp=1;
  while(nome[i]){
    push(nome[i++],p);
  }
  i=0;
  while(nome[i]){
	  char c = pop(p);
    if (nome[i++]!=c) { 
		resp=0;
		printf("Digite seu nome: ");
		printf("%s != %c",nome[i],c);
	}
	else printf("teste");

  }
  printf(resp == 1 ? "Palindromo\n" : "Nao e palindromo\n");
  return 0;
}