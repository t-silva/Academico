#include<stdio.h>
int main(void){
    int v[7]={1,9,3,4,19,2,5},x;
    for (int i=1;i<=6;i++)
        for (int j=0;j<7-i;j++){
            if(v[j]>v[j+1]){
                x=v[j];
                v[j]=v[j+1];
                v[j+1]=x;
                
            }
        }
    for (int i=0;i<=6;i++) printf("%d\n",v[i]);
    return 0;
}