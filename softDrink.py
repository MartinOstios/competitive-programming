data_input = input().split(" ")
(n, k, l, c, d, p, nl, np) = [int(x) for x in input().split(" ")]
# n = int(data_input[0]) # friends
# k = int(data_input[1]) # bottles
# l = int(data_input[2]) # milimiters
# c = int(data_input[3]) # limes
# d = int(data_input[4]) # slices
# p = int(data_input[5]) # salt
# nl = int(data_input[6]) # toast: quantity of milimiters of drink
# np = int(data_input[7]) # toast: quantity of salt

# toast = (k*l) / nl, (c*d), (p/np)
value1 = (k*l) / nl
value2 = c*d
value3 = p/np
print(int(min(value1, value2, value3) // n))