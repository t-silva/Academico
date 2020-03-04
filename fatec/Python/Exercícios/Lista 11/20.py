from random import randint
print(" ________________________________________________")
print("|                                                |")
print("|          Ordenando valores aleatórios          |")
print("|________________________________________________|")
N = input("\nDigite a quantidade de elementos para ordenar: ")
while not N.isnumeric():
    print(" _____________________________________________")
    print("|                                             |")
    print(f"|   ✘ Valor precisa ser um número inteiro! ✘  |")
    print("|_____________________________________________|")

    N = input("\nDigite a quantidade de elementos para ordenar: ")
N = int(N)
lista = []
for a in range(N):
    lista.append(randint(-1000,1000)) #Como o exercício não estipulou o intervalo, defini como
                                      # de -1000 a 1000 (inteiros, contando negativos)
tam_lista = len(lista)
#print(lista)
for i in range(tam_lista):
    #print(f'---- i ={i} -----\nTroca = False')
    troca = False
    for j in range(1,tam_lista-i):
       # print(f'j ={j}')
        if lista[j] < lista[j-1]:
            lista[j],lista[j-1] = lista[j-1],lista[j]
            troca = True # Se trocar uma vez, não entra no próximo IF, e continua no looping
    if not troca: #Otimizando, se passar uma vez sem trocar nada, break
        break
#Formatando output e imprimindo lista"

print("\nOrdenando Lista...")
print("----------------------------")
print(f"\nLista ordenada = {lista}\n")
print("----------------------------")
print('Fim do programa')

