meow = ["\o", "m", "e", "o", "w", "\o"]

def isACat(s, n):
    if n < 4: return False
    s = s.lower()
    k = 0
    for n in s:
        if n != meow[k]:
            if n == meow[k+1]:
                k += 1
            else:
                return False
    return k==4

t = int(input())
for i in range (t):
    n = int(input())
    s = input()
    if(isACat(s, n)):
        print("YES")
    else:
        print("NO")