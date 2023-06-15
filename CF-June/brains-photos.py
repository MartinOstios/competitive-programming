'''
Problem: https://codeforces.com/problemset/problem/707/A
Difficulty: 800
Tries: 1
Time: 15m
'''

(n, _) = [int(x) for x in input().split()]

def f():
    for i in range(n):
        line = input().split()
        for letter in line:
            if letter in ['C', 'M', 'Y']:
                return False
    return True

print('#Black&White' if f() else '#Color')
