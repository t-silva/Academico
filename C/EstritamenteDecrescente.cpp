#include<stdio.h>
int main(void){
    int v[7]={20,9,8,7,6,5,4}; //vetor já organizado **importante para funcionar**
    for (int i=0;i<=6;i++){ //percorre todos os elementos do vetor.
        if(v[i+1]==v[i]) return printf("Decrescente\n"); //considerando que ele já está organizado, pega cada elemento v[[i] e compara com o pŕoximo
    }                                                     // para ser estritamente decrescente, não podem ter valores iguais,
                                                        // então se ele achar um igual, já retorna decrescente.
    return printf("estritamente decrescente\n"); //se não acha nenhum valor igual, posso falar que é estritamente decrescente
}
