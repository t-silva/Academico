listaA = []
listaB = []
R = []
nA = input("Informe o tamanho da 'LISTA A': ")
while not nA.isnumeric():
    N = input("\nNúmero informado precisa ser inteiro\nInforme o tamanho da 'LISTA A': ")
nA = int(nA)

print('Montando lista A')
count = 1
while len(listaA) < nA:
    VALOR = input(f"Digite o {count}o valor: ")
    while VALOR.isnumeric() == False:
        print(f'\nO valor precisa ser um número inteiro')
        VALOR = input(f"Digite o {count}o valor: ")
    if int(VALOR) in listaA:
        print(f'\n{VALOR} já está na lista')
    else:
        listaA.append(int(VALOR))
        count +=1
#Começando lista B
nB = input("Informe o tamanho da 'LISTA B': ")
while not nB.isnumeric():
    N = input("\nNúmero informado precisa ser inteiro\nInforme o tamanho da 'LISTA B': ")
nB = int(nB)
count = 1
print('----------------------------------------\nMontando lista B')
while len(listaB) < nB:
    VALOR = input(f"Digite o {count}o valor: ")
    while VALOR.isnumeric() == False:
        print(f'\nO valor precisa ser um número inteiro')
        VALOR = input(f"Digite o {count}o valor: ")
    if int(VALOR) in listaB:
        print(f'\n{VALOR} já está na lista')
    else:
        listaB.append(int(VALOR))
        count +=1
R = listaA
for a in range(len(listaB)):
    if listaB[a] not in R:
        R.append(listaB[a])

print(f'Lista Resultando tem {len(R)} elementos\nR = {R}')
