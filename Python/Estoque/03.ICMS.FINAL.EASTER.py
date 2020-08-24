from calendar import monthrange
from datetime import date,datetime
import random
from random import randint
from decimal import Decimal
'''
 - PROGRAMA LE E GERA LISTA
 - FAZ CALCULO DAS VENDAS DE ACORDO COM PRODUTOS QUE TEM NO ESTOQUE, ACABOU O PRODUTO, ELE REMOVE DAS VENDAS
 - VENDE ALEATORIAMENTE A QUANTIDADE DE PRODUTOS DE ACORDO COM DIAS DE VENDAS E COM O TOTAL EM ESTOQUE.
 - Se o produto acabou no estoque, remove o produto da lista e vende o que tem em loja
 - Quando acabar todo estoque, recarrega lendo novamente o arquivo
 - Quantidade mínima para venda de produtos por peso em 0.5, para evitar vendas com valores insignificantes
 - Gera relatório de venda e de folgas
 - Troca automaticamente se data de término for maior que de início
'''
ESP = QREC = SP = SE = ZFM = DUF = 0
RECARGA = False
LDESC = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
def monta_tabela(line,char):
    global OPCAO
    TAMTAB = 70
    TAMNOME = len(char)
    if line == 1:
        print(f'╔{char*TAMTAB}╗ ')
    elif line ==0:
        print(f'╠{char*TAMTAB}╣')
    elif line == 2:
        print(f'█{char:^{TAMTAB}}█')
    elif line == 3:
        print(f'╚{char*TAMTAB}╝ ')
    elif line == 5:
        if char == '':
            print(f'║{"║":->{TAMTAB+1}}')
        else:
            print(f'█{char*TAMTAB}█')
    elif line == 7:
        print(f'█  {char:>{TAMTAB-3}} █')
    elif line == 8:
        print(f'█  {char:<{TAMTAB-3}} █')
    elif line == 9:
        OPCAO = input(f'║{" "*(TAMTAB-10-len(char))}{char}')
        return OPCAO    
def recarrega():
    global RECARGA,QREC
    QREC +=1
    if not RECARGA:
        print('\n'*2)
        monta_tabela(1,'═')
        monta_tabela(2,'!!!!!!! ESTOQUE VAZIO, RECARREGANDO !!!!!! ')
        monta_tabela(0,'═')
        monta_tabela(2,'')
        monta_tabela(8,'A quantidade de vendas realizadas excede o estoque, a partir de')
        monta_tabela(8,' agora ESSA MENSAGEM NÃO SERÁ EXIBIDA NOVAMENTE! As recargas ')
        monta_tabela(8,'SERÃO AUTOMÁTICAS e um relatório será exibido ao fim do programa.')
        monta_tabela(5,'')
        monta_tabela(9,'Pressione <ENTER> para recarregar o estoque')
        monta_tabela(3,'▬')
        RECARGA = True
    leitura()
def aliquota():
    global UF,SP,SE,ZFM,DUF
    ICMS = [('São Paulo',18),('Sudeste e Sul',12),('Zona Franca de Manaus',0),('Demais UFs',7)]
    IND = randint(0,len(ICMS)-1)
    UF = ICMS[IND]
    if IND == 0:
        SP+=1
    elif IND == 1:
        SE +=1
    elif IND == 2:
        ZFM +=1
    elif IND ==3:
        DUF +=1
def gravacao(LVENDAS):
    global TTOTAL
    OUTPUT = open("VENDAS.txt", 'w')
    LINHAS = 0
    for a in LVENDAS:
        OUTPUT.writelines(f'{a}\n')
        LINHAS+=1
    OUTPUT.close()
    monta_tabela(5,'░')
    monta_tabela(0,'═')
    monta_tabela(2,'RELATORIO DE VENDAS')
    monta_tabela(0,'═')
    monta_tabela(2,f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    monta_tabela(2,f'O PROGRAMA REALIZOU {LINHAS:,} VENDAS')
    monta_tabela(2,f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    monta_tabela(2,'')
    monta_tabela(8,f'                - São Paulo: {SP} VENDAS.')
    monta_tabela(8,f'                - Sudeste e Sul: {SE} VENDAS.')
    monta_tabela(8,f'                - Zona Franca de Manaus: {ZFM} VENDAS.')
    monta_tabela(8,f'                - Demais UFs: {DUF} VENDAS.')
    monta_tabela(2,'')
    monta_tabela(0,'═')
    monta_tabela(2,f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    monta_tabela(2,f' {ESP:,} VENDAS RECEBERAM PREÇO ESPECIAL ')
    monta_tabela(2,f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    monta_tabela(2,'')
    monta_tabela(7,f'* Valor Aleatório esperado {LINHAS:,} x 0.35 = {float(LINHAS*0.35):,.2f}')
    monta_tabela(0,'═')
    monta_tabela(2,f'FORAM REALIZADAS {QREC} RECARGAS NO ESTOQUE')
    monta_tabela(3,'▬')
def leitura():
    global LISTA
    INPUT = open("PRODUTOS.txt")
    LISTA=[]
    S = INPUT.readline()
    while S != '':
        L = S.rstrip().split(';')
        LISTA.append([L[0],L[1],L[2],L[3],L[4]])
        S = INPUT.readline()
    INPUT.close()
def calc_preco(CUSTO,LUCRO,QTD):
    global ValorVenda,ESP
    ValorUnid = CUSTO * (1+(LUCRO/100))
    if randint(1,100) <= 35:
        PORC = random.choice(LDESC)/100
        FATOR = 1+PORC
        ESP+=1
        ValorVenda = ValorUnid*FATOR
    else:
        ValorVenda = ValorUnid
    aliquota()
    ValorVenda = round((ValorVenda * (1+UF[1]/100)),2)
    return ValorVenda
def VENDAFUNC(ANO,MES,DIA,QtdeVendasDia):
    global TABPROD,Qven,ValorVenda
    VENDA = 1
    while VENDA <= QtdeVendasDia:
        if len(LISTA) == 0:
            recarrega()
        IndCod = randint(0,len(LISTA)-1)
        PRODUTO = int(LISTA[IndCod][0])
        a = 0
        ACHOU = False
        while a <= len(LISTA)-1 and not ACHOU:
            if str(PRODUTO) in LISTA[a]:
                ACHOU = True
                TABPROD = (LISTA[a])
                if TABPROD[1] == 'P':
                    if float(TABPROD[2]) % 1 != 0:
                        Qven = round(random.uniform(0.5,(float(TABPROD[2])/2)),3)
                    else:
                        Qven = round(random.uniform(1,float(TABPROD[2])/2),0)
                    RESTA = round(float(TABPROD[2])-Qven,3)
                    if RESTA <= 0.5:
                        Qven += RESTA
                        RESTA = 0
                        TABPROD[2] = f'{RESTA:.3f}'
                        LISTA.remove(TABPROD)
                    else:
                        TABPROD[2]= f'{RESTA:.3f}'
                        LISTA[a] = TABPROD
                    Qven = f'{Qven:.3f}'
                elif TABPROD[1] =='U':
                    Qven = randint(1,int(TABPROD[2]))
                    RESTA = int(TABPROD[2])-Qven
                    if RESTA ==0:
                        LISTA.remove(TABPROD)
                    else:
                        TABPROD[2] = f'{RESTA}'
                        LISTA[a] = TABPROD
            a+=1
        VENDA+=1
        calc_preco(float(TABPROD[3]),float(TABPROD[4]),float(Qven))
        VRealizada = f'{ANO};{str(MES).zfill(2)};{DIA};{PRODUTO};{Qven};{ValorVenda};{UF[0]};{UF[1]}'
        LVENDAS.append(VRealizada)
def range_date():
    global LVENDAS,DOM,ANO,ANO2,MES,MES2,DIA,DIA2#,INICIO
    monta_tabela(1,'═')
    monta_tabela(2,'INICIANDO')
    monta_tabela(0,'═')
    def cabecalho():
        global ANO,ANO2,MES,MES2,DIA,DIA2
        ANO=ANO2=MES=MES2=DIA=DIA2=0
        monta_tabela(9,'Digite a data de início DD/MM/AAAA: ')
        DATA1 = OPCAO.split('/')
        while len(DATA1)!=3:
            monta_tabela(5,'-')
            monta_tabela(2,'Entrada inválida')
            monta_tabela(5,'-')
            monta_tabela(9,'Digite a data de início DD/MM/AA: ')
            DATA1 = OPCAO.split('/')
        while not DATA1[0].isdigit() or not DATA1[1].isdigit() or not DATA1[2].isdigit() or int(DATA1[2])<2016  \
              or int(DATA1[2])>9999 or int(DATA1[1]) <1 or int(DATA1[1])>12 or int(DATA1[0])<1\
              or int(DATA1[0]) > monthrange(int(DATA1[2]),int(DATA1[1]))[1]:
            if DATA1[0].isdigit() and DATA1[1].isdigit() and DATA1[2].isdigit():
                if int(DATA1[2])<2016:
                    monta_tabela(5,'-')
                    monta_tabela(2,'Ano de início deve ser maior que 2016')
                    monta_tabela(5,'-')
                elif int(DATA1[2])>9999:
                    monta_tabela(5,'-')
                    monta_tabela(2,'Futuro muito distante, o mundo já acabou')
                    monta_tabela(5,'-')
                elif int(DATA1[1]) <1 or int(DATA1[1])>12:
                    monta_tabela(5,'-')
                    monta_tabela(2,'Mes deve estar entre 01-12')
                    monta_tabela(5,'-')
                elif int(DATA1[0]) > monthrange(int(DATA1[2]),int(DATA1[1]))[1]:
                    monta_tabela(5,'-')
                    monta_tabela(2,f'{DATA1[1]}/{DATA1[2]} tem {monthrange(int(DATA1[2]),int(DATA1[1]))[1]} dias')
                    monta_tabela(5,'-')
            else:
                monta_tabela(5,'-')
                monta_tabela(2,'Entrada inválida')
                monta_tabela(5,'-')
            monta_tabela(9,'Digite a data de início DD/MM/AAAA: ')
            DATA1 = OPCAO.split('/')
        DIA = int(DATA1[0])
        MES = int(DATA1[1])
        ANO = int(DATA1[2])
        monta_tabela(0,'▬')
        monta_tabela(9,'Digite a data de término DD/MM/AA: ')
        DATA2 = OPCAO.split('/')
        while len(DATA2)!=3:
            monta_tabela(5,'-')
            monta_tabela(2,'Entrada inválida')
            monta_tabela(5,'-')
            monta_tabela(9,'Digite a data de início DD/MM/AA: ')
            DATA2 = OPCAO.split('/')
        while not DATA2[0].isdigit() or not DATA2[1].isdigit() or not DATA2[2].isdigit() or int(DATA2[2])<2016 \
              or int(DATA2[2])>9999 or int(DATA2[1]) <1 or int(DATA2[1])>12 or int(DATA2[0])<1 \
              or int(DATA2[0]) > monthrange(int(DATA2[2]),int(DATA2[1]))[1]:
            if DATA2[0].isdigit() and DATA2[1].isdigit() and DATA2[2].isdigit():
                if int(DATA2[2])<2016:
                    monta_tabela(5,'-')
                    monta_tabela(2,'Ano de término deve ser maior que 2016')
                    monta_tabela(5,'-')
                elif int(DATA1[2])>9999:
                    monta_tabela(5,'-')
                    monta_tabela(2,'Futuro muito distante, o mundo já acabou')
                    monta_tabela(5,'-')
                elif int(DATA2[1]) <1 or int(DATA2[1])>12:
                    monta_tabela(5,'-')
                    monta_tabela(2,'Mes deve estar entre 01-12')
                    monta_tabela(5,'-')
                elif int(DATA2[0]) > monthrange(int(DATA2[2]),int(DATA2[1]))[1]:
                    monta_tabela(5,'-')
                    monta_tabela(2,f'{DATA1[1]}/{DATA1[2]} tem {monthrange(int(DATA1[2]),int(DATA1[1]))[1]} dias')
                    monta_tabela(5,'-')

            else:
                monta_tabela(5,'-')
                monta_tabela(2,'Entrada inválida')
                monta_tabela(5,'-')
            monta_tabela(9,'Digite a data de TÉRMINO DD/MM/AAAA: ')
            DATA2 = OPCAO.split('/')
        DIA2 = int(DATA2[0])
        MES2 = int(DATA2[1])
        ANO2 = int(DATA2[2])
    cabecalho()
    while datetime(ANO2,MES2,DIA2) < datetime(ANO,MES,DIA):
        monta_tabela(5,'-')
        monta_tabela(2,'ANO DE TERMINO MENOR QUE DE INÍCIO')
        monta_tabela(5,'-')
        cabecalho()
    monta_tabela(0,'═')
    monta_tabela(9,'Digite a quantidade de vendas por dia: ')
    while not OPCAO.isdigit():
        monta_tabela(5,'-')
        monta_tabela(2,'Entrada inválida')
        monta_tabela(5,'-')
        monta_tabela(9,'Digite a quantidade de vendas por dia: ')
    monta_tabela(3,'▬')
    monta_tabela(0,'═')
    monta_tabela(2,f'Calculando vendas entre {DIA}/{MES}/{ANO} e {DIA2}/{MES2}/{ANO2}')
    monta_tabela(0,'═')
    QtdeVendasDia = int(OPCAO)
    LVENDAS = []
    DOM = []
    while ANO<= ANO2:
        FIM = False
        FIMMES = False
        while (MES <= MES2 or ANO<=ANO2) and not FIMMES:
            NDIASMES = monthrange(ANO,MES)
            while DIA <= NDIASMES[1] and not FIM:
                if date(ANO,MES,DIA).weekday() != 6:
                    VENDAFUNC(ANO,MES,DIA,QtdeVendasDia)
                else:
                    DOM.append((DIA,MES,ANO))
                if DIA == DIA2 and MES == MES2 and ANO==ANO2:
                    FIM = True
                DIA +=1
            DIA = 1
            if MES < 12 and not FIM:
                MES+=1
            else:
                FIMMES = True
        MES = 1
        ANO+=1
    print('\n')
    monta_tabela(1,'▬')
    monta_tabela(2,' IMPRIMINDO RELATÓRIOS ')
    monta_tabela(0,'▬')
    monta_tabela(5,'░')
    monta_tabela(0,'═')
    monta_tabela(2,'TABELA DE FOLGAS')
    monta_tabela(0,'═')
    monta_tabela(2,f'O periodo informado teve {len(DOM)} domingos:')
    monta_tabela(0,'═')
    monta_tabela(9,'Deseja visualizar as datas? (s/n)')
    monta_tabela(0,'═')
    if OPCAO.lower() =='s':
        for a in DOM:
            monta_tabela(2,f'{str(a[0]).zfill(2)}/{str(a[1]).zfill(2)}/{a[2]}')
        monta_tabela(0,'═')
def calcula_mes():
    global LVENDAS,INICIO
    monta_tabela(1,'═')
    monta_tabela(2,'INICIANDO')
    monta_tabela(0,'═')
    monta_tabela(9,'DIGITE O ANO: ')
    while not OPCAO.isdigit() or not (2015 < int(OPCAO) <= 9999 ):
        if OPCAO.isdigit() and int(OPCAO)<2016:
            monta_tabela(5,'')
            monta_tabela(2,'Ano deve ser superior a 2016')
            monta_tabela(5,'')
        elif OPCAO.isdigit() and int(OPCAO)>9999:
            monta_tabela(5,'')
            monta_tabela(2,'Futuro muito distante, o mundo já acabou!')
            monta_tabela(2,'')
##            monta_tabela(2,'      _.-^^---....,,--         ')
##            monta_tabela(2,' _--                  --_      ')
##            monta_tabela(2,' <                        >)   ')
##            monta_tabela(2,' |                         |   ')
##            monta_tabela(2,' \._                   _./     ')
##            monta_tabela(2," ```--. . , ; .--'''           ")
##            monta_tabela(2,"           | |   |             ")
##            monta_tabela(2,"        .-=||  | |=-.          ")
##            monta_tabela(2,"       `-=#$%&%$#=-'          ")
##            monta_tabela(2,"          | ;  :|             ")
##            monta_tabela(2,"_.,-#%&$@%#&#~,._   ")
##            monta_tabela(2,'')
            monta_tabela(2,"________________")
            monta_tabela(2,"____/ (  (    )   )  \___")
            monta_tabela(2,'/( (  (  )   _    ))  )   )\"')
            monta_tabela(2,"((     (   )(    )  )   (   )  )")
            monta_tabela(2,'((/  ( _(   )   (   _) ) (  () )  )')
            monta_tabela(2,"( (  ( (_)   ((    (   )  .((_ ) .  )_")
            monta_tabela(2,"( (  )    (      (  )    )   ) . ) (   )")
            monta_tabela(2,"(  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")
            monta_tabela(2,"( (  (   ) (  )   (  ))     ) _)(   )  )  )")
            monta_tabela(2,"( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")
            monta_tabela(2,"(  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")
            monta_tabela(2,"( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")
            monta_tabela(2,"((  (   )(    (     _    )   _) _(_ (  (_ )")
            monta_tabela(2,"(_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")
            monta_tabela(2,"((__)        \\||lll|l||///          \_))")
            monta_tabela(2,"   /(/ (  )  ) )\   ")
            monta_tabela(2,'    ( ( ( | | ) ) )\   ')
            monta_tabela(2,"   /(| / ( )) ) ) )) ")
            monta_tabela(2,'     ( ((((_(|)_)))))     ')
            monta_tabela(2,'      ||\(|(|)|/||     ')
            monta_tabela(2,'        |(||(||)||||        ')
            monta_tabela(2,'     //|/l|||)|\\ \     ')
            monta_tabela(2,'/ / //  /|//||||\\  \ \  \ _)')
            monta_tabela(5,'')
        else:
            monta_tabela(5,'')
            monta_tabela(2,'Entrada inválida')
            monta_tabela(5,'')
        monta_tabela(9,'DIGITE O ANO: ')
    ANO = int(OPCAO)
    monta_tabela(0,'═')
    monta_tabela(9,'Digite o Mês: ')
    while not OPCAO.isdigit() or (int(OPCAO) < 1 or int(OPCAO) > 12):
        if OPCAO.isdigit():
            monta_tabela(5,'')
            monta_tabela(2,'Mês incorreto, deve ser entre 01-12')
            monta_tabela(5,'')
        else:
            monta_tabela(5,'')
            monta_tabela(2,'Entrada Inválida')
            monta_tabela(5,'')
        monta_tabela(9,'DIGITE O MÊS: ')
    MES = int(OPCAO)
    monta_tabela(0,'═')
    monta_tabela(9,'Digite a quantidade de vendas ao dia: ')
    while not OPCAO.isdigit():
        monta_tabela(5,'')
        monta_tabela(2,'Entrada inválida')
        monta_tabela(5,'')
        monta_tabela(9,'Digite a quantidade de vendas ao dia: ')
    QtdeVendasDia = int(OPCAO)
    DIASMES = monthrange(int(ANO),int(MES))
    NDiasMes = DIASMES[1]
    DIA = 1
    DOM = []
    LVENDAS = []
    monta_tabela(3,'▬')
    while DIA <= NDiasMes:
        if date(ANO,MES,DIA).weekday() != 6:
            VENDAFUNC(ANO,MES,DIA,QtdeVendasDia)
        else:
            DOM.append(DIA)
        DIA+=1
    print('\n'*3)
    monta_tabela(1,'▬')
    monta_tabela(2,' IMPRIMINDO RELATÓRIOS ')
    monta_tabela(0,'▬')
    monta_tabela(5,'░')
    monta_tabela(0,'═')
    monta_tabela(2,'TABELA DE FOLGAS')
    monta_tabela(0,'═')
    monta_tabela(2,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    monta_tabela(2,f'O MÊS DE VENDAS TEVE {len(DOM)} DOMINGOS:')
    monta_tabela(2,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    monta_tabela(2,'')
    LDOM = ''
    for a in DOM:
        if DOM.index(a) == len(DOM)-2:
            LDOM +=str(a).zfill(2)+f'/{str(MES).zfill(2)}/{ANO} e '
        elif DOM.index(a) == len(DOM)-1:
            LDOM +=str(a).zfill(2)+f'/{str(MES).zfill(2)}/{ANO}.'
        else:
            LDOM +=str(a).zfill(2)+f'/{str(MES).zfill(2)}/{ANO}, '
    monta_tabela(2,LDOM)
    monta_tabela(2,'')
    monta_tabela(0,'═')
def inicio():
    global LVENDAS
    monta_tabela(1,'═')
    monta_tabela(2,'PROGRAMA DE VENDAS')
    monta_tabela(0,'═')
    monta_tabela(8,'~~~~~~~~')
    monta_tabela(8,'  MENU  ')
    monta_tabela(8,'~~~~~~~~')
    monta_tabela(8,'1 - Gerar vendas para um mês.')
    monta_tabela(8,'2 - Gerar vendas para um período.')
    monta_tabela(5,'')
    monta_tabela(9,'OPÇÃO: ')
    while OPCAO != '1' and OPCAO != '2':
        monta_tabela(9,'OPÇÃO: ')
    monta_tabela(3,'▬') 
    if OPCAO == '1':      
        leitura()
        calcula_mes()
    elif OPCAO == '2':
        leitura()
        range_date()
    gravacao(LVENDAS)
    SAIR = input("Aperte <ENTER> para sair")
inicio()
