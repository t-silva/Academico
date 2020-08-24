#include<stdio.h>
#define max 10
typedef struct{
    int fim;
    int s[10];
}Fila;
int vazia(Fila *f){ return f->fim==0;}
void init(Fila *f){ f->fim=0;}
void exibe(Fila *f){
	if(!vazia(f)){
		printf(" -----");
		for(int i=1;i<=(f->fim*4);i++) printf("-");
		printf("\n| Fila: " );
	    for (int i = 1; i<=f->fim;i++) printf("%d, ",f->s[i]);
		printf("\n -----");
		for(int i=1;i<=(f->fim*4);i++) printf("-");
	    puts("");
	}
	else printf("FILA VAZIA\n");
}
void troca(Fila *f, int n, int j){
    int aux = f->s[n];
    f->s[n] = f->s[j];
    f->s[j] = aux;
}
void fixup(Fila *f){
    int aux = f->fim;
    while ((f->s[aux] > f->s[aux/2]) && aux!=1){
        printf("Elemento com maior prioridade, trocando...\n");
        troca(f,aux/2,aux);
        aux/=2;
    }
    exibe(f);
}
void atende(Fila *f){
    int atendeu=f->s[1];
    f->s[1]=f->s[f->fim];
    f->s[f->fim--] = atendeu;
	printf("\n==================\n");
    printf("Atendendo: %d...\n",atendeu);
	printf("==================\n");
    exibe(f);
}
void fixdown(Fila *f){
    printf("ORGANIZANDO FILA!....\n");
    int elemento = 1;
    int f_esq = 2;
    int f_dir = 3;
	if(f->fim > 2)
		while(f->fim > f_esq){
	        if (f->s[f_esq] > f->s[f_dir]){
	        	if (f->s[f_esq]>f->s[elemento]) {
	                troca(f,f_esq,elemento);
	                elemento = f_esq;
	            }
			}
	       	else if(f->s[f_dir] > f->s[f_esq]){    
				if (f->s[f_dir] > f->s[elemento]) {
	                troca(f,f_dir,elemento);
	                elemento = f_dir;
	            }
			}
	  		f_esq = elemento*2;
    		f_dir = elemento*2+1;   
		}
	else 
		if (f->s[f->fim] > f->s[elemento]) 
			troca(f,f->fim,elemento); 
    exibe(f);
}
int main(void){
    Fila f1;
    Fila *f=&f1;
    init(f);
    int num;
    do{
    	printf("Insira um elemento na fila\n(0 para iniciar atendimento): ");
    	scanf("%d",&num);
    	if (num!=0){
    	    f->s[++f->fim] = num;
    	    fixup(f);
    	}
    }while(num!=0);
    int resp;
	int count=0;
    do{
		printf("-------------------------------------------------\n");
        printf("Digite 1 enquanto quiser atender a fila: ");
        scanf("%d",&resp);
        if(resp==1) {
            atende(f);
			if (f->fim > 1) fixdown(f);
			count++;
        }
    }while(resp==1 && !vazia(f)); 
	printf("Ordem de Atendimento: ");
	for (int i = 1; i<=count;i++) printf("%d,",f->s[i]);
	puts("");
	return 0;
}
