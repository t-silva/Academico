#Defindo função para checar se número é FLOAT
def is_number(num):
    try:
        float(num)
        #If successful, returns true.
        return True
    except:
        #Silently ignores any exception.
        pass
    return False

###############################################
lista = []
print(" _________________________________")
print("|                                 |")
print("|___Ordenando valores positivos___|")
print("|_Digite 0 ou negativo para sair._|")
print("|_________________________________|")

N = 1
while N > 0:
    N = input("\n| Digite um valor positivo: ")
    print("|_____________________________")
    while not is_number(N):
        print(" ______________________________________")
        print("|                                      |")
        print(f"|  ✘ Valor digitado não é um número ✘  |")
        print("|______________________________________|")
        N = input("\n| Digite um valor positivo: ")
        print("|_____________________________")
    N = float(N)
    
    if N > 0:
        if len(lista) == 0:
            lista.append(N)
        else:
            tamanho = len(lista)
            val = 1
            count = 0
            while count < tamanho and val == 1:      
                if N < lista[count]:
                    print(f'{N} < {lista[count]}')
                    lista.insert(count,N)
                    val = 0
                count +=1
            if val ==1:
                print(f'{N} é o maior')
                lista.append(N)
                
print("\nOrdenando Lista...",)
print("-----------------", end="")
for a in range(len(lista)):
    print(f'{"-"* len(str(lista[a]))}--',end="")
print(f"\nLista ordenada = {lista}")
print("-----------------", end="")
for a in range(len(lista)):
    print(f'{"-"* len(str(lista[a]))}--',end="")
    

