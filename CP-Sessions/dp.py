import math
r = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 5
cant1 = 0
cant2 = 0
def vn_function(n):
    if n <= 0:
        return 0 
    if n == 1:
        return r[1]
    v = r[n]
    for i in range(1, math.ceil(n/2) + 1):
        cant1+=1
        c = vn_function(n - i) + vn_function(i)
        if c > v: v = c
    return v

def opt(n):
    if n==0: return 0
    max = 0
    for i in range(1, n+1):
        v = r[i] + opt(n-i)
        cant2 += 1
        if v > max:
            max = v
    return max

def test():
    cant1 = 0
    cant2 = 0
    print([vn_function(i) for i in range(1,11)])
    print([opt(i) for i in range(1,11)])
    print(cant1)
    print(cant2)

test()





