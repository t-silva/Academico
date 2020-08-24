N = 51
lista= []
while N < 0 or N > 50:
    N = int(input("Digite o número de elementos [0-50]: "))
if N != 0:
    for a in range(N):
        valor = input(f"Digite o elemento {a+1}º da lista: ")
        lista.append(valor)
    print("Lista = {}" .format(lista))
else:
    print("Lista vazia")
