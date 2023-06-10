
def result(n, data):
    for i in range(n - 1):
        if data[i] == 1:
            data[i] +=1
        if(data[i+1] % data[i] == 0):
            data[i+1] += 1
        
    return data



t = int(input())
for i in range (t):
    n = int(input())
    data = [int(x) for x in input().split(" ")]
    resultado = " ".join([str(x) for x in result(n, data)])
    print(resultado)