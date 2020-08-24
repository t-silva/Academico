N = 51
A = []
POS = []
NEG = []
while N < 0 or N > 50:
    N = int(input("Digite o número de elementos [0-50]: "))
for a in range(N):
    A.append(float(input(f"Digite o {a+1} valor: ")))
for b in range(N):
    if A[b] < 0:
        NEG.append(A[b])
    elif A[b] >= 0:
        POS.append(A[b])
print("-----------------------------------------------")
print(f"A lista de números negativos contém {len(NEG)} elementos \nLista NEGATIVA = {NEG}" if len(NEG) != 0 else "Lista negativa Vazia")  
print("_______________________________________________\n")
print(f"A lista de números positivos contém {len(POS)} elementos \nLista POSITIVA = {POS}" if len(POS) !=0 else "Lista positiva Vazia")
print("-----------------------------------------------")
