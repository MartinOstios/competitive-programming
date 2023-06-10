'''
Problem: https://codeforces.com/problemset/problem/490/A
Difficulty: 800
Tries: 2
Time: 30m
'''

_ = input()
data = [int(x) for x in input().split(" ")]
q_teams = min([data.count(i) for i in range(1, 4)])
print(q_teams)
value_printed = []
for i in range(q_teams):
    for j in range(1, 4):
        #for k, value in enumerate(data):
        index = data.index(j)
        value = data[index]
        data[index] = 0
        if index not in value_printed:
            print(index + 1, end=" ")
            value_printed.append(index)
    print()

