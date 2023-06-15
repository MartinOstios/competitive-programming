'''
Problem: https://codeforces.com/problemset/problem/1370/A
Difficulty: 800
Tries: 1
Time: 15m
'''

def gcd(a, b):
    if a != b:
        value = min(a,b)
        while a % value != 0 or b % value != 0:
            value -= 1
        return value
    return -1

t = int(input())
values = []
for i in range(t):
    n = int(input())
    for j in range (1, n + 1):
        for k in range(j, n + 1):
            value = gcd(j, k)
            values.append(int(value))
    print(max(values))