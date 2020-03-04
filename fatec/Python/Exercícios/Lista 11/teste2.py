def is_number(num):
    try:
        float(num)
        #If successful, returns true.
        return True
    except:
        #Silently ignores any exception.
        pass
    return False
N = "a"
while not is_number(N):
    print("Não é número real")
