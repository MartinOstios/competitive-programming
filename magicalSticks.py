import math
t = int(input())

for i in range(t):
    n = int(input())
    if n != 1:
        print(math.ceil((n)/2))
    else:
        print("1")