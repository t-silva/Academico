#include<stdio.h>
int *soma(int a[2][3], int b[2][3],int c[2][3], int m, int n){
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			c[i][j]=a[i][j]+b[i][j];
			}
	}
printf("C = ");
	for(int i=0;i<m;i++){
		printf("| ");
		for(int j=0;j<n;j++){
			printf("%d ", c[i][j]);
			}
	printf("|\n    ");
	}
	puts("");
return *c;
}
int main(void){
	int m=2,n=3;	
	int a[2][3] = {
		{1,2,3},
		{1,2,3}
		};
	int b[2][3] = {
		{1,2,3},
		{1,2,3}
	};
	int c[2][3];
	//soma(a,b,c,m,n);
	printf("Endereço da matriz: %P\n",soma(a,b,c,m,n));
}
