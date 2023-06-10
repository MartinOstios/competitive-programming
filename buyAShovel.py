def cantShovel(k, r):
    cont = 2
    value = k
    while (value % 10 != r and value % 10 != 0):
        value = k * cont
        cont+=1 
    return cont
        



(k, r) = [int(x) for x in input().split()]
print(cantShovel(k, r) - 1)
