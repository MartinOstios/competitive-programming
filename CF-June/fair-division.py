'''
Problem: https://codeforces.com/problemset/problem/1472/B
Difficulty: 800
Tries: 1
Time: 10m
'''

t = int(input())
for i in range(t):
    _ = input()
    data = [int(x) for x in input().split()]
    sumatoria = sum(data)
    if sumatoria % 2 == 0:
        half = len(data) // 2
        if sum(data[:half]) == sumatoria // 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")