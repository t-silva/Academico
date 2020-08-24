N = int(input())
i = 0
P = 1
while P < N:
    P = 2+i*2
    QP = P**2
    print("%i^2 = %i" % (P,QP))
    i+=1
