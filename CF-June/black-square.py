'''
Problem: https://codeforces.com/problemset/problem/431/A
Difficulty: 800
Tries: 1
Time: 5m
'''

num_values = [x for x in input().split(" ")]
s = input()

calories = 0
for letter in s:
    calories += int(num_values[int(letter) - 1])
print(calories) 