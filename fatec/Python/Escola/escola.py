# GRUPO 1 
# NOMES:
# Eduardo Tavares Vicente Maria 18200280
# Paulo Humberto Anhaia Negrelli 19100056
# Robson dos Santos Pereira 19100548
# Thiago da Silva 19100332
'''
Funcionalidades EXTRAS :
 1) Tabela se ajusta sozinha de acordo com tamanho do maior nome da lista
 2) Nomes grandes tem sobrenomes abreviados, utilizando o maior nome como referência.
 3) Impressão de boletim com tamanho autoajustável de acordo com o NOME do aluno
 4) Caso rode no IDLE, (RUN MODULE F5) programa imprime cores de acordo com a situação final
 5) notas até .9 são arredondadas para cima
 6) Grafico com distribuição de notas.
 7) Filtro por situação
 8) Pesquisa por parte de nomes de alunos
'''
def final():
    global OPCAO
    monta_tabela(9,'DIGITE A OPÇÃO: ')
    monta_tabela(3,'═')
    def sub_menu(classe):
            monta_tabela(1,'═')
            monta_tabela(2,f'{classe}')
            monta_tabela(0,'═')
            monta_tabela(8,'======')
            monta_tabela(8,' MENU:')
            monta_tabela(8,'======')
            monta_tabela(8,"0 - VOLTAR")
            monta_tabela(0,'═')
    while OPCAO != '0' and OPCAO !='1':
        if OPCAO == '2':
            sub_menu('BOLETIM POR MATRÍCULA')
            monta_tabela(9,'DIGITE A MATRICULA: ')
            monta_tabela(3,'═')
            while OPCAO != '0':
                if OPCAO.isnumeric() and len(OPCAO)!=9 and OPCAO !='1' and OPCAO !='0':
                        #print('\n')
                        monta_tabela(1,'═')
                        monta_tabela(2,"!!! ERRO: A MATRÍCULA CONTÉM 9 DÍGITOS !!!")
                        monta_tabela(3,'═')
                elif OPCAO.isnumeric() and len(OPCAO)==9:
                    encontrado = False
                    for a in dados:
                        if OPCAO == a[0] and not encontrado:
                            TamCampoNome = len(a[1])
                            boletim(a,TamCampoNome)
                            encontrado = True
                    if not encontrado:
                        #print('\n')
                        monta_tabela(1,'═')
                        monta_tabela(2,"!!! ERRO: MATRÍCULA NÃO ENCONTRADA !!!")
                        monta_tabela(3,'═')
                sub_menu('BOLETIM POR MATRÍCULA')
                monta_tabela(9,'DIGITE A MATRICULA: ')
                monta_tabela(3,'═')
            monta_tabela(5,'')    
        elif OPCAO == '3':
            sub_menu('PESQUISAR NOME DE ALUNO')
            monta_tabela(2,'Aperte <ENTER> para ver todos...')
            monta_tabela(0,'▬')
            monta_tabela(9,'BUSCAR POR: ')
            monta_tabela(3,'═')
            while OPCAO !='0':
                AUXTAB=[]
                encontrado = False
                for a in dados:
                    if OPCAO.lower() in a[1].lower():
                        AUXTAB.append(a)
                        encontrado= True
                if len(AUXTAB) == 1:
                    ALIST = AUXTAB[0]
                    TamCampoNome = len(ALIST[1])
                    boletim(AUXTAB[0],TamCampoNome)
                elif len(AUXTAB)>1:
                    monta_tabela(1,'═')
                    monta_tabela(7,f'{len(AUXTAB)} NOMES ENCONTRADOS')
                    monta_tabela(7,f'Utilize os índices para escolher')
                    monta_tabela(0,'▬')
                    monta_tabela(9,'Aperte <ENTER> para continuar...')
                    monta_tabela(0,'═')
                    indices=[]
                    for i,a in enumerate(AUXTAB):
                        indices.append(str(i+1))
                        monta_tabela(2,f'{i+1}) {a[1]}')
                        monta_tabela(2,f'Matricula: {a[0]}')
                        monta_tabela(5,'')
                    monta_tabela(9,'Índice: ')
                    monta_tabela(3,'═')
                    #print('\n')
                    while OPCAO not in indices:
                        monta_tabela(2,'ÍNDICE INVÁLIDO')
                        monta_tabela(9,'Índice: ')
                    ALIST = AUXTAB[int(OPCAO)-1]
                    TamCampoNome = len(ALIST[1])
                    boletim(AUXTAB[int(OPCAO)-1],TamCampoNome)
                elif not encontrado:
                    monta_tabela(1,'═')
                    monta_tabela(2,'Nenhum aluno encontrado')
                    monta_tabela(1,'═')
                sub_menu('PESQUISAR NOME DE ALUNO')
                monta_tabela(9,'BUSCAR POR: ')
                monta_tabela(3,'═')
        elif OPCAO == '4':
            estatistica()
        elif OPCAO == '5':
            while OPCAO != '0':
                if OPCAO =='1':
                    tab_alunos(1)
                elif OPCAO =='2':
                   tab_alunos(2)
                elif OPCAO != '5':
                    monta_tabela(2,'OPÇÃO INVÁLIDA')
                sub_menu('FILTRAR POR SITUAÇÂO')
                monta_tabela(8,'1 - APROVADOS')
                monta_tabela(8,'2 - REPROVADOS')
                monta_tabela(5,'')   
                monta_tabela(9,'FILTRAR POR: ')
                monta_tabela(5,'')
                
        else:
            monta_tabela(2,'OPÇÃO INVÁLIDA')
        inicio()
        monta_tabela(9,'DIGITE A OPÇÃO: ')
        monta_tabela(3,'═')
    if OPCAO =='1':
        reinicia()
def calcula_media(n1, n2, n3):
    MEDIA = 0.1 * (4 * n1 + 4 * n2 + 2 * n3)
    if MEDIA % 0.1 != 0:
        MEDIA = round((MEDIA - MEDIA % 0.1 + 0.1),2)
    return MEDIA
def check_name(nome,TamCampoNome):
    while len(nome) > TamCampoNome:
        LN = nome.split() 
        MN = max(LN[1:len(LN)-1],key=len) 
        PMN = LN.index(MN)
        NM = MN[0] 
        LN[PMN] = f'{NM}.' 
        nome =''
        for a in LN:
            nome += f'{a} '
    return nome
def boletim(aluno,TamCampoNome):
    global TAMTAB
    TAMAUX = TAMTAB
    if TamCampoNome <= 15:
        TamCampoNome = 15
    monta_tabela(1,'═')
    monta_tabela(2,'IMPRIMINDO BOLETIM')
    monta_tabela(0,'═')
    monta_tabela(2,f'{"~"*TamCampoNome}')
    monta_tabela(2,'BOLETIM')
    monta_tabela(2,f'{"~"*TamCampoNome}')
    nome = check_name(aluno[1],TMN)
    monta_tabela(2,nome)
    monta_tabela(2,aluno[0])
    monta_tabela(2,f'{"Prova 1: "}{" ":.>{TamCampoNome-12}}{float(aluno[2])}')
    monta_tabela(2,f'{"Prova 2: "}{" ":.>{TamCampoNome-12}}{float(aluno[3])}')
    monta_tabela(2,f'{"Trabalho: "}{" ":.>{TamCampoNome-13}}{float(aluno[4])}')
    MD = calcula_media(float(aluno[2]), float(aluno[3]), float(aluno[4]))
    monta_tabela(2,f'{"Média: "}{" ":.>{TamCampoNome-10}}{str(MD)}')
    monta_tabela(2,f'{"~"*TamCampoNome}')
    print(f'{"█":<{int((TAMAUX/2)-2)}}', end="")
    if MD >= 6:
        if IDLE:
            color.write("APROVADO","STRING")
        else:
            print("APROVADO",end="")
        print(f'{"█":>{int((TAMAUX/2)-3)}}')
    else:
        if IDLE:
            situacao = color.write("REPROVADO","ERROR")
        else:
            print("REPROVADO", end="")
        print(f'{"█":>{int((TAMAUX/2)-4)}}')
    print(f'█{"~" * TamCampoNome:^{TAMAUX}}█')
    monta_tabela(3,'═')
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
def inicio():
    monta_tabela(1,'═')
    monta_tabela(8,'=================')
    monta_tabela(8,' MENU PRINCIPAL:')
    monta_tabela(8,'=================')
    monta_tabela(8,'1 - LISTAR TODOS')
    monta_tabela(8,'2 - BOLETIM POR MATRÍCULA')
    monta_tabela(8,'3 - PESQUISAR')
    monta_tabela(8,'4 - GRÁFICO ESTATÍSTICO')
    monta_tabela(8,'5 - FILTRAR POR SITUAÇÃO')
    monta_tabela(8,'0 - SAIR')
    monta_tabela(0,'═')
def maior_nome():
    global TAMTAB,TMN,dados
    arq = open("ALUNOS.txt",encoding = "ISO-8859-1")
    A = arq.readline()
    L = []
    dados=[]
    while A != "":
        L = A.rstrip().split(";")
        dados.append(L)
        A = arq.readline()
    MN = 'a'
    for a in range(len(dados)):
        L = dados[a]
        NOME = str(L[1])
        if len(NOME) > len(MN):
            MN = NOME
    TMN = len(MN)
    if 30 < TMN < 70:
        TMN -= int(len(MN)*0.1)
    elif 70<= TMN < 120:
        TMN -= int(len(MN)*0.2)
    elif TMN >= 120:
        TMN-=int(len(MN)*0.3)
    if TMN % 2 != 0:
        TMN +=1
    TAMTAB = TMN + 11 + 5+10 +7
    if TAMTAB % 2 ==0:
        TAMTAB+=1
    arq.close()
def check_IDLE():
    global IDLE,color
    import sys
    try:
        color = sys.stdout.shell
        IDLE = True
    except:
        IDLE = False
        monta_tabela(1,'═')
        monta_tabela(2,'Para uma melhor experiência, utilize o')
        monta_tabela(2,'')
        monta_tabela(2,"RUN MODULE (F5) do IDLE")
        monta_tabela(2,'')
        monta_tabela(2,"o progama apresentará cores")
        monta_tabela(1,'═')
        pass
def tab_alunos(tipo):
    global CODIGO,ALUNO,MEDIA,TOTAL,AUXT
    print(f'║  {"CODIGO":<11} {"NOME DO ALUNO":<{TMN}}  {"MEDIA":^5}'+
              f'  {"SITUACAO":<9} ║')
    print(f'║  {"-"*11} {"-"*TMN}  {"-"*5}'+
              f'  {"-"*10}║')
    PARC = 0
    for a in range(len(dados)):
        L = dados[a]
        CODIGO = int(L[0])
        ALUNO = check_name(L[1],TMN)
        MEDIA = calcula_media(float(L[2]), float(L[3]), float(L[4]))
        if tipo ==1 and MEDIA >=6:
            monta_tabela(4,ALUNO)
            PARC+=1
            SIT = 'APROVADO(S)'
        elif tipo ==2 and MEDIA < 6:
            monta_tabela(4,ALUNO)
            PARC+=1
            SIT = 'REPROVADO(S)'
        elif tipo ==3:
            monta_tabela(4,ALUNO)
            if not AUXT:
                TOTAL +=1
    AUXT = True
    monta_tabela(0,'═')
    if tipo == 3:
        monta_tabela(2,f'{TOTAL} ALUNOS CADASTRADOS')
    else:
        monta_tabela(2,f'{PARC} ALUNOS {SIT}( {round(PARC*100/TOTAL,2)}% )')
    monta_tabela(3,'▬')
def estatistica():
    monta_tabela(1,"═")
    monta_tabela(2,"GRÁFICO DE DISTRIBUIÇÃO DE NOTAS")
    monta_tabela(0,"═")
    TOTAL = N1 = N2 = N3 = N4 = N5 = N6 = N7 = N8 = N9 = N10 = 0
    for a in dados:
        TOTAL +=1
        MEDIA = calcula_media(float(a[2]),float(a[3]),float(a[4]))
        if MEDIA <=1:
            N1+=1
        elif 1<MEDIA<=2:
            N2+=1
        elif 2<MEDIA<=3:
            N3+=1
        elif 3<MEDIA<=4:
            N4+=1
        elif 4<MEDIA<=5:
            N5+=1
        elif 5<MEDIA<=6:
            N6+=1
        elif 6<MEDIA<=7:
            N7+=1
        elif 7<MEDIA<=8:
            N8+=1
        elif 8<MEDIA<=9:
            N9+=1
        elif 9<MEDIA<=10:
            N10+=1
    PROP = TAMTAB-20
    E1 = f' (0,0→1)┤{"▓"*int((N1/TOTAL)*PROP)} ~{round((N1/TOTAL)*100,2)}%'
    E2 = f' (1,1→2)┤{"▓"*int((N2/TOTAL)*PROP)} ~{round((N2/TOTAL)*100,2)}%'
    E3 = f' (2,1→3)┤{"▓"*int((N3/TOTAL)*PROP)} ~{round((N3/TOTAL)*100,2)}%'
    E4 = f' (3,1→4)┤{"▓"*int((N4/TOTAL)*PROP)} ~{round((N4/TOTAL)*100,2)}%'
    E5 = f' (4,1→5)┤{"▓"*int((N5/TOTAL)*PROP)} ~{round((N5/TOTAL)*100,2)}%'
    E6 = f' (5,1→6)┤{"▓"*int((N6/TOTAL)*PROP)} ~{round((N6/TOTAL)*100,2)}%'
    E7 = f' (6,1→7)┤{"▓"*int((N7/TOTAL)*PROP)} ~{round((N7/TOTAL)*100,2)}%'
    E8 = f' (7,1→8)┤{"▓"*int((N8/TOTAL)*PROP)} ~{round((N8/TOTAL)*100,2)}%'
    E9 = f' (8,1→9)┤{"▓"*int((N9/TOTAL)*PROP)} ~{round((N9/TOTAL)*100,2)}%'
    E10 = f'(9,1→10)┤{"▓"*int((N10/TOTAL)*PROP)} ~{round((N10/TOTAL)*100,2)}%'
    GRAF = f'         {"┴"*(PROP)}100%'
    monta_tabela(8," NOTAS")
    monta_tabela(8,E1)
    monta_tabela(8,E2)
    monta_tabela(8,E3)
    monta_tabela(8,E4)
    monta_tabela(8,E5)
    monta_tabela(8,E6)
    monta_tabela(8,E7)
    monta_tabela(8,E8)
    monta_tabela(8,E9)
    monta_tabela(8,E10)
    monta_tabela(8,GRAF)
    monta_tabela(3,'═')
def reinicia():
    maior_nome()
    inicio()
    monta_tabela(2,' SISTEMAS DE NOTAS ')
    monta_tabela(5,' ')
    tab_alunos(3)
    inicio()
    monta_tabela(2,'Selecione a ação de acordo com o MENU PRINCIPAL')
    monta_tabela(0,'▬')
    final()
TOTAL = 0
AUXT = False
maior_nome()
check_IDLE()
monta_tabela(1,'═')
monta_tabela(2,' ')
monta_tabela(2,'MAXIMIZE SUA JANELA')
monta_tabela(2,'PARA MELHOR VISUALIZAÇÂO DA TABELA')
monta_tabela(2,' ')
monta_tabela(3,'═')
resp = input('\nAperte <ENTER> para continuar...')
reinicia()
monta_tabela(1,'═')
monta_tabela(2,'SAINDO...')
monta_tabela(0,'▬')
monta_tabela(2,'GRUPO 1 - IAL002')
monta_tabela(3,'═')
