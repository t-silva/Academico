//Valia posfixa
int avalia_posfixa(char pos[]){
	Pilha *p;int i,x,y,z;
	p = malloc(sizeof(Pilha));
	if(p==NULL){
		printf("> !! problema na alocacao");
		exit(1);
	}
	init(p);
	for(i=0;pos[i];i++){
		if((pos[i]>='0')&& (pos[i]<='9'))
			push(pos[i]-'0',p); //o -'0' pega o valor na tabela ASCII 
		else {					//e devolve o character que quero representar
			y=pop(p);x=pop(p);
			if (pos[i]=='+') push (x+y,p);
			if (pos[i]=='-') push (x-y,p);
			if (pos[i]=='*') push (x*y,p);
			if (pos[i]=='/') push (x/y,p);
		}
	}
	z=pop(p);
	free(p);
	return z;
}
