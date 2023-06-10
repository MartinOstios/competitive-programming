data = []
def insert_data():
    i = 0
    while(len(data) != 1000):
        i += 1
        if i % 3 != 0:
            if i % 10 != 3:
                data.append(i)


insert_data()
t = int(input())
for i in range (t):
    k = int(input())
    print(data[k-1])

