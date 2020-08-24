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


void inf_to_pos(char inf[], char pos[]){
	int i,j=0;
	Pilha p1;   //struct
	Pilha *p = &p1;
	if(p==NULL){
		printf("> !! problema na alocacao");
		exit(1);
	}
	init(p);
	for(int i=0; inf[i]!='\0';i++){ //dentro de um for, não faz diferença '++i' ou 'i++'
		switch(inf[i]){
			case '('	:	break;
			case ')'	:	{pos[j++]=pop(p);break;}
			case '+'	:   
			case '-'	:   
			case '*'	:   
			case '/'	:	{push(inf[i],p); break;}
			default		:	pos[j++]= inf[i];
		}
	}
}
int main(void){
    char inf[20];
    char pos[20];
    inf_to_pos(inf,pos);
    fgets(inf,20,stdin);
    inf_to_pos(inf,pos);
	for (int i=0;pos[i];i++) printf("%c",pos[i]);
    //puts(pos);
}