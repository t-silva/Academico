LISTA = []
Min = input("Digite um valor mínimo: ")

while not Min.lstrip('-+').isnumeric():
    Min = input("\nO valor deve ser inteiro!\nDigite um valor mínimo: ")
Min = int(Min)

PASS = 0

while PASS != 1:
    Max = input("Digite um valor máximo: ")
    if not Max.lstrip('-+').isnumeric():
        print("\nO valor deve ser inteiro!")
        PASS = 0
    else:
        Max = int(Max)
        if Max <= Min:
            print('\nValor máximo precisa ser maior que mínimo')
        else:
            PASS = 1
VALOR = Min
while VALOR <= Max:
    if VALOR % 7 == 0:
        LISTA.append(VALOR)
    VALOR+=1
print(f"Lista = {LISTA}" if len(LISTA) != 0 else f'Não há valores entre {Min} e {Max} divisíveis por 7')
        
