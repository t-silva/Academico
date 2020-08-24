//protótipo da função, só apresentação.
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef int obj;
#define max 100
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
	if(isfull(p)) {printf("!!! stack overflows\n"); exit(1);} //checa se pilha está cheia;
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
  char s[61];
  int conf =1;
  printf("Digite a sequência: ");
  fgets(s, 61, stdin);
  for (int i=0;s[i];i++) {
	  switch (s[i])
	  {
	  case '(': push(s[i],p); break;
	  case '[': push(s[i],p); break; 
	  case ')': if (!isempty(p) && pop(p)!='(') conf=0; break;
	  case ']' : if (!isempty(p) && pop(p)!='[') conf=0; break;
	  default: conf=0;
	  }
  }
  printf(conf==1? "Correto" : "Incorreto");

  return 0;
}