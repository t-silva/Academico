lista = []
lista = input().split(" ")
for a in range(len(lista)):
    lista[a] = int(lista[a])
T = ((lista[2] - lista[0])*60) + (lista[3] - lista[1])
if T >= 1 and T <= 1440:
    H = T // 60
    M = T % 60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)" .format(H,M))
elif (lista[2] - lista[0]) == lista[3] - lista[1] == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

