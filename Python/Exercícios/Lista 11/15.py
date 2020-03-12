from random import randint
nA = int(input("Digite o Tamanho da Lista 1: "))
nB = int(input("Digite o Tamanho da Lista 2: "))
L1 = []
L2 = []
for a in range(nA):
    L1.append(randint(1,100))
for a in range(nB):
    L2.append(randint(1,100))
LISTA = L1 + L2
print(f"LISTA = {LISTA}")
