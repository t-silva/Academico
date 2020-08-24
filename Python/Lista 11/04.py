from random import randint
N = 51
lista= []
while N < 0 or N > 50:
    N = int(input("Digite o número de elementos [0-50]: "))
if N != 0:
    for a in range(N):
        lista.append(randint(0, 1000))
    print("Lista = {}" .format(lista))
else:
    print("\nLista vazia")

