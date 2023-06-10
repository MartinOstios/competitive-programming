t = int(input())

for i in range (t):
    test = [int(x) for x in input()]
    part1 = test[0:3]
    part2 = test[3:]
    if(sum(part1) == sum(part2)):
        print("YES")
    else:
        print("NO")
