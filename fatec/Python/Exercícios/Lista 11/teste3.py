for a in range(10):
    print(f'Primeiro for a = {a}')
    print('Troca = False')
    troca = False
    for j in range(1,10-a):
        N = input(f"Segundo for J = {j}\nQuer continuar? ")
        if N == 'Y' or N == 'y':
            troca = True
            print("Continuando, TROCA = True")
        if not troca:
            print("parando....")
            break
        
