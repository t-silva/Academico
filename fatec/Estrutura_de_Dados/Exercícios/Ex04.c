#include<stdio.h>
#include<string.h>
int busca(char c,char s[]){
	for (int i=0;s[i];i++){
		if (s[i]!=c) printf("%c != %c\n",s[i],c);
		else return 1;
		}
	return 0;
}
int main(void){
	char s[52],ch;
	scanf("%s",s);
	scanf(" %c",&ch);
	printf("%d\n",busca(ch,s));
return 0;
}
