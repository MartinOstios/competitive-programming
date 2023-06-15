'''
Problem: https://codeforces.com/problemset/problem/1360/A
Difficulty: 800
Tries: 3
Time: 1h
'''
t = int(input())
for i in range(t):
    (a, b) = [int(x) for x in input().split()]
    c = min(a, b)
    c *= 2
    side = max(a, b, c)
    print(side ** 2)
    