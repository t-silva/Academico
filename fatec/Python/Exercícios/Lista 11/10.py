from random import randint
LISTA = []
N = int(input("Quantos números aleatórios deseja gerar? "))
count = 1
while count <= N:
    RAND = randint(0,10)
    LISTA.append(RAND)
    count +=1
print(f"Lista = {LISTA}")
X = int(input("Digite um valor para consultar na lista: "))
QTD = len(LISTA)
count = 0
P = 0
while count <= (QTD-1):
    if LISTA[count] == X:
        print(f"O número {X} está presente na posição {count} da lista")
        P = 1
    count+=1
if P != 1:
    print(f"O número {X} não está presente na lista")
