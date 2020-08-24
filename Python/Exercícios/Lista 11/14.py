L1=[]
L2=[]
print("FORMANDO PRIMEIRA LISTA.....")
for a in range(10):
    N = input(f"Digite o {a+1}o valor para lista 1: ")
    while N.isnumeric() == False:
        N = input(f"Valor não aceito! O {a+1}o valor deve ser do tipo inteiro:\nTente novamente: ")
    L1.append(int(N))

print("..............................................")
print("FORMANDO SEGUNDA LISTA.....")
for a in range(10):
    N = input(f"Digite o {a+1}o valor para lista 2: ")
    while N.isnumeric() == False:
        N = input(f"Valor não aceito! O {a+1}o valor deve ser do tipo inteiro:\nTente novamente: ")
    L2.append(int(N))
LISTA = L1 + L2
print("Lista final = {}" .format(LISTA))
   
