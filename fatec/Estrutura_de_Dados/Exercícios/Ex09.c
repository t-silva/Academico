#include<stdio.h>
void exibe(int m[], int tam){
	printf("Matriz C = [");
	for (int i=0;i<tam;i++){
		printf("%d,",m[i]);
	}	
	printf("]\n");
}
void intercala(int s[],int m,int b[],int n){
	int c[m+n],o=0,aux=0,tam;
	for(int i=0;i<m;i++){
		for(int j=0+aux;j<n;j++){
			if(b[j]<s[i]){ c[o++]=b[j];aux++;}
			else {c[o++]=s[i];break;} 
		}
		if(aux==n) c[o++]=s[i];
	}
	if(aux<n) for(int j=0+aux;j<n;j++)c[o++]=b[j];
	tam=sizeof(c)/sizeof(c[1]);
	printf("Tamanho da nova matriz: %d\n",tam);
	exibe(c,tam);
}
int main(void){
	int a[15]={1,3,5,7,9,11,13,15,17,19,21,23,25,27,29};
	int m=sizeof(a)/sizeof(a[0]);
	int b[14]={2,4,6,8,10,12,14,16,18,20,22,24,26,28};
	int n=sizeof(b)/sizeof(b[0]);
	intercala(a,m,b,n);
return 0;}
