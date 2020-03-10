N = int(input())
IN = 0
OUT = 0
for i in range(1,N+1):
    X = int(input())
    if (-10**7) <= X <= (10**7):
        if 10 <= X <= 20:
            IN +=1        
        else:
            OUT +=1
print("%i in" %IN)
print("%i out" %OUT)
