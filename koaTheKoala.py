t = int(input())
for i in range(t):
    (n, a, b) = [int(x) for x in input().split(" ")]
    if a + b <= n:
        print("Si se puede procesar")
    else:
        print("No")