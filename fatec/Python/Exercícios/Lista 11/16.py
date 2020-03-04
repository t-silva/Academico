N = input("Informe o tamanho da lista: ")
while N.isnumeric() == False:
    N = input("\nNúmero informado precisa ser inteiro\nInforme o tamanho da Lista: ")
N = int(N)
PRESENT = 0
LISTA = []
count = 1
while len(LISTA) < N:
    VALOR = input(f"Digite o {count}o valor: ")
    while VALOR.isnumeric() == False:
        print(f'\nO valor precisa ser um número inteiro')
        VALOR = input(f"Digite o {count}o valor: ")
    if int(VALOR) in LISTA:
        print(f'\n{VALOR} já está na lista')
    else:
        LISTA.append(int(VALOR))
        count +=1
print(f'LISTA = {LISTA}')
