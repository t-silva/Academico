#include<stdio.h>
int main(void){
	int n,maior;
	scanf("%d",&n);
	while(n<1){printf("n>=1\n");scanf("%d",&n);}
	int v[n];
	for (int i=0;i<n;i++) {
		printf("%do numero: ",i+1);
		scanf(" %d",&v[i]);
	}
	maior=v[0];
	for(int j=0;j<n;j++) v[j]=0;
	printf("[");
	for(int j=0;j<n;j++) printf(" %d,",v[j]);
	printf("]\n");
return 0;}
