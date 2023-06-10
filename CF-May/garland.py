
def get_repeated_digits(s):
    dict = {}
    # Revisar cuantos digitos repetidos hay
    for word in s:
        if word in dict:
            dict[word] = dict[word] + 1
        else:   
            dict[word] = 1
    return max(dict.values())
    


t = int(input())
for i in range (t):
    s = input()
    repeated_digits = get_repeated_digits(s)
    if repeated_digits == 1 or repeated_digits == 2:
        print("4")
    if repeated_digits == 3:
        print("6")
    if repeated_digits == 4:
        print("-1")