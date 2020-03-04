X = int(input())
if 1<= X <=1000:
    count = 0
    impar = 0
    while impar < X-1:
        impar=(1+2*count)
        count += 1
        print(impar)
