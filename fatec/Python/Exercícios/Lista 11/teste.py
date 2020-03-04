N = int(input())
LISTA = []
for a in range(N):
    VALOR = input()
    if VALOR.isnumeric() == False:
        INT = 0
    else:
        INT = 1

    if VALOR in LISTA:
        PRESENT = 1
    else:
        PRESENT = 0
    LISTA.append(VALOR)
