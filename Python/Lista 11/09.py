from random import randint
LISTA = []
N = int(input("Quantos números aleatórios deseja gerar? "))
for a in range(N):
    RAND = randint(0,1000)
    LISTA.append(RAND)
print(f"Lista = {LISTA}")
