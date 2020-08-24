SALARIO = float(input(''))
if SALARIO >= 0 and SALARIO <=400:
    R = 0.15
    NS = 1.15*SALARIO
    PC = '15'
elif SALARIO <= 800:
    NS = 1.12*SALARIO
    PC = '15'
elif SALARIO <= 1200:
    NS = 1.10 * SALARIO
    PC = '10'
elif SALARIO <= 2000:
    NS = 1.07 * SALARIO
    PC = "7"
elif SALARIO > 2000:
    NS = 1.04 * SALARIO
    PC = '4'
print("Novo salario: %.2f" %NS)
print("Reajuste ganho: %.2f" %(NS-SALARIO))
print("Em percentual: " + str(PC) + " %")
#print("Novo salario: {:.2f} " .format(NS))
#print('Reajuste ganho: {:.2f} '.format(NS - SALARIO))
#print('Em percentual: {} %'.format(PC))
