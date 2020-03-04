N = int(input("Digite um valor máximo para saber os N primeiros números primos: "))
while N !=0:
        
    if N == 0:
        print("Saindo...")
        exit()
    count = 1
    NUM = 3
    TOTAL = 0
    LISTA = [2]
    if N > 1:
        while count <= N-1:
            DIV = 2
            PRIMO=0
            while DIV < NUM:
                if NUM % DIV != 0:
                    PRIMO = 1
                    #print(f'{NUM}/{DIV} dá resto != 0')
                    DIV+=1
                else:
                    PRIMO = 0
                    DIV = NUM
                
            if PRIMO == 1:
                TOTAL+=1
                LISTA.append(NUM)
                count+=1
            NUM+=1
    print("     ", end="") # dá o espaçamento da primeira linha
    for a in range(len(LISTA)):
        print('_______', end="") # para cada elemento da lista, adiciona 6 "_" para a linha superior
    print('\n    │',end="") # dá espaçamento e coloca uma | no começo da lista
    for a in range(len(LISTA)): 
        print('      │', end="") # para cada elemento dá 6 espaços e coloca mais uma barra
        
    print(f'\nV = │', end="") # coloca o V = | 
    for a in range(len(LISTA)):
        print(f'  0{LISTA[a]}  │' if LISTA[a] < 10 else f'  {LISTA[a]}  │', end="") #para cada elemento printa na lista com 6 espaçamentos sempre
                                                                                    # se o lemento for >= 10, coloca só 5 para compensar o digito a mais
                                                                                    #e ficar com 6 espaçamentos sempre
    print("     ", end="") #começa a parte de baixo da tabela com espaço para alinhar
    print('\n    │',end="") # coloca o | para iniciar a tabela
    for a in range(len(LISTA)):
        print('______│', end="") # para cada elemento coloca 6 "_" e fecha aquela célula com "|"
        
    N = int(input("\n\nDigite um valor máximo para saber os N primeiros números primos: "))
