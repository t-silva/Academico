N = int(input("Digite o número de elementos da lista: "))
if N > 0:
    lista = []
    indice = 1
    for a in range(N):
        lista.append(int(input(f"Digite {indice}o elemento: ")))
        indice +=1
print(f'\nLista = {lista}\n-----------------------------------------')
a=0
while a < len(lista):
    print(f"\nProcurando repetições do {a}º elemento = {lista[a]}.....\n")
    b = a+1 #forçando novo índice+1, para não deletar o primeiro valor encontrado
    while b < len(lista):#início do While, varrendo a partir do valor +1 até fim da lista
        if lista[a] == lista[b]: # se for encontrado valor semelhante
            print(f"Deletando repetição do valor {lista[a]} encontrado no índice = {b}") #Avisa que foi encontrado e em qual posição
            del(lista[b]) #deleta elemento de maior índice (b)
            #nao há incremento, pois se encontrar valor repetido, ao deletar, o próximo valor se for repetido
            #não será deletado, pois assumirá o índice do elemento anterior
            print(f'Nova lista = {lista}')
        else:
            
            b+=1 #aumenta o indice em 1 e volta a procurar
    a+=1
print(f"\n---------------------------------\nNova lista sem repetições = {lista}")
