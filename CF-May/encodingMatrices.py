binary_dict = {'0': 0, '1': 0}
cont = 0
def getValues(line):
    for word in line:
        binary_dict[word] = binary_dict[word] + 1

def printResult():
    if binary_dict['0'] > binary_dict['1']:
        result = "\n".join(array).replace('0', '*').replace('1', 'o')
    elif binary_dict['1'] > binary_dict['0']:
        result = "\n".join(array).replace('1', '*').replace('0', 'o')
    else:
        if array[0][0] == '0':
            result = "\n".join(array).replace('0', '*').replace('1', 'o')
        else:
            result = "\n".join(array).replace('1', '*').replace('0', 'o')
    print(result)

array = []
n = int(input())
for i in range(n):
    line = input()
    getValues(line)
    array.append(line)
printResult()   
