from random import randint
lista = []
N = int(input("Digite a quantidade de números a gerar: "))
for a in range(N):
    lista.append(randint(1,1000))
print(f'Lista = {lista}')
X = int(input("Digite um valor para remover da Lista: "))
aux = 1
while aux == 1:
    if X not in lista:
        aux =0
    else:
        index = lista.index(X)
        del(lista[index])
        
print(f"Lista sem o valor {X} = {lista}")
    
