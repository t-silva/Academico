def monta_tabela(line,char):
    global OPCAO
    TAMNOME = len(char)
    if line == 1:
        print(f'╔{char*TAMTAB}╗ ')
    elif line ==0:
        print(f'╠{char*TAMTAB}╣')
    elif line == 2:
        print(f'█{char:^{TAMTAB}}█')
    elif line == 3:
        print(f'╚{char*TAMTAB}╝ ')
    elif line == 4:
        print(f'█  {CODIGO:<11} {char:.<{TMN}}  {MEDIA:^5}  ',end="")
        if MEDIA >= 6:
            if IDLE:
                color.write("APROVADO ","STRING")
            else:
                print(f'{"APROVADO "}',end="")
        else:
            if IDLE:
                color.write("REPROVADO","ERROR")
            else:
                print(f'{"REPROVADO"}',end="")
        print(f' █')
    elif line == 5:
        print(f'║{"║":->{TAMTAB+1}}')
    elif line == 6:
        L6 = char.split(";")
        if TAMTAB/2 % 2 != 0:
            TABAUX = int((TAMTAB+1)/2)
        else:
            TABAUX = int(TAMTAB/2)
        print(f'║  {L6[0]:<{TABAUX-2}}{L6[1]:>{(TABAUX-1)}} ║')
    elif line == 7:
        print(f'█  {char:>{TAMTAB-3}} █')
    elif line == 8:
        print(f'█  {char:<{TAMTAB-3}} █')
    elif line == 9:
        OPCAO = input(f'║{" "*(TAMTAB-9-len(char))}{char}')
LISTA = [['Jan',8],['Fev',8],['Marc',17],['Abr',11],['Mai',19],['Jun',25.3],['Jul',11],['Ago',30],['Set',7],['Out',9],['Nov',13],['Dez',10]]
SOMA=SOMPERC=0
LGRAF=[]
for a in LISTA:
    SOMA+=a[1]
for a in LISTA:
    PERC = a[1] *100/SOMA
    SOMPERC+=PERC
    LGRAF.append([a,PERC])
MAIOR = round(max(LGRAF, key=lambda x:x[1])[1])
TAMTAB = len(LISTA)*7
PROP = MAIOR+5
monta_tabela(1,'═')
monta_tabela(2,"Gráfico aleatório")
monta_tabela(0,'═')
while PROP > 0:
    LINHA = ''
    if PROP%5!=0:
        LINHA+=f'{"":<4}'
    else:
        LINHA+=f'{PROP:>2}╠▬'
    for i in LGRAF:
        if round(i[1]) == PROP-1:
            LINHA+=f'{i[1]/100:^6.1%}' if PROP%5!=0 else f'{i[1]/100:▬^6.1%}'
        elif round(i[1])== PROP:
            LINHA+=f'{"█████":^6}' if PROP%5!= 0 else f'{"█████":▬^6}'
            i[1]-=1
        else:
            LINHA+=f'{"":^6}' if PROP%5!=0 else f'{"":▬^6}'
    monta_tabela(2,LINHA)
    PROP-=1
monta_tabela(2,f'     {"══⋃═══"*len(LISTA)}')
LINHA = ''
for a in LISTA:
    LINHA+=f'{a[0]:^6}'
monta_tabela(2,LINHA)
monta_tabela(3,'═')
X = input("Digite <ENTER> para sair")
