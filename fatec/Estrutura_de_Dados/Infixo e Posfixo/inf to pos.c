void inf_to_pos(char inf[], char pos[]){
	int i,j=0;
	Pilha *p;   //struct
	p = malloc(sizeof(Pilha));
	if(p==NULL){
		printf("> !! problema na alocacao");
		exit(1);
	}
	init(p);
	for(int i=0; inf[i]!='\0';++i) //dentro de um for, não faz diferença '++i' ou 'i++'
		switch(inf[i]){
			case '('	:	break;
			case ')'	:	{pos[j++]=pop(p);break;}
			case '+'	:
			case '-'	:
			case '*'	:
			case '/'	:	{push(inf[i],p); break;}
			default		:	pos[j++]= inf[i];
		}
	pos[j]='\0';
	free(p);
}
