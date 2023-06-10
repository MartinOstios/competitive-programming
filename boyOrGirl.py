result = []
string = input()

for x in string:
    if x not in result:
        result.append(x)

if len(result) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
