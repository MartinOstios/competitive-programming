morze = input()
result = ""

flag = False
for char in morze:
    if char == "-" and flag == False:
        flag = True
        continue
    
    if flag == True:
        if char == ".":
            result += "1"

        if char == "-":
            result += "2"

        flag = False
    else:
        result += "0"


print(result)
