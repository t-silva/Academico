lista = []
count = len(lista)
while count != 10:
    lista = input("Digite 10 elementos para a lista (separado por espaço)").split(" ")
    count = len(lista)
for valor in reversed(lista):
    indice = lista.index(valor)
    print("Indice {} da lista: {}" .format(indice,valor))
