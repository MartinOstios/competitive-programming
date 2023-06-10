t = int(input())

for i in range (t):
    x = 0
    rating = int(input())
    if rating >= 1900:
        x = 1
    if rating >= 1600 and rating <= 1899:
        x = 2
    if rating >= 1400 and rating <= 1599:
        x = 3
    if rating <= 1399:
        x = 4
    print("Division ", x)