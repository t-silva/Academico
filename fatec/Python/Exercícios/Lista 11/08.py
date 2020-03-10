A = []
R = []
LMin = int(input("Digite o valor mínimo do intervalo a ser computado: "))
LMax = int(input("Digite o valor máximo do intervalo a ser computado: "))
if LMax < LMin:
    print("Valor Mínimo ({}) maior que Máximo({}), invertendo valores..." .format(LMin,LMax))
    aux = LMin
    LMin = LMax
    LMax = aux
    print("LMin = {} | LMax = {}" .format(LMin,LMax))
N = int(input("Quantos números deseja computar? "))
if N > 0:
    for x in range(N):
        VALOR = int(input("Digite um valor: "))
        if LMax >= VALOR >= LMin:
            A.append(VALOR)
        else:
            R.append(VALOR)
    print("-----------------------------------------------------------------")
    print("Valores dentro do Intervalo [{},{}] \nA = {}" .format(LMin,LMax,A))
    print("Tamanho da lista A = {}" .format(len(A)))
    print("-----------------------------------------------------------------")
    print("Valores fora do intervalor R = {}" .format(R))
    print("Tamanho da lista R = {}" .format(len(R)))
    print("-----------------------------------------------------------------")
else:
    print("Saindo...")
