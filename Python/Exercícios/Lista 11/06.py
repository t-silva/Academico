LMin = int(input("Digite o valor mínimo do intervalo a ser computado: "))
LMax = int(input("Digite o valor máximo do intervalo a ser computado: "))
A = []
if LMax < LMin:
    print("Valor Mínimo ({}) maior que Máximo({}), invertendo valores..." .format(LMin,LMax))
    aux = LMin
    LMin = LMax
    LMax = aux
    print("LMin = {} | LMax = {}" .format(LMin,LMax))
for x in range(10):
    VALOR = int(input("Digite um valor: "))
    if LMax >= VALOR >= LMin:
        A.append(VALOR)
print("Valores dentro do Intervalo [{},{}] = {}" .format(LMin,LMax,A))
print("Tamanho da lista A = {}" .format(len(A)))
    
