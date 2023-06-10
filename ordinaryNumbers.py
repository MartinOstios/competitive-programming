def ordinaryNumbers(n):
    count = 0
    for i in range (1, 10):
        start = i
        while(start<=n):
            count += 1
            start = start*10+i
        
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(ordinaryNumbers(n))


