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
	for(int j=1;j<n;j++) if(v[j]>maior) maior=v[j];
	printf("%d\n",maior);	
return 0;}
