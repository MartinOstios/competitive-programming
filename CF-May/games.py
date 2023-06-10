teams = []

def hostPlaysWithGuestUniform(host, guest):
    if host[0] == guest[1]:
        return True
    else:
        return False
    

n = int(input())
for i in range(n):
    team = [int(x) for x in input().split(" ")]
    teams.append(team)

sum = 0
for i in range (len(teams)):
    for team in teams:
        if teams[i] != team:
            if hostPlaysWithGuestUniform(teams[i], team):
                sum += 1

print(sum)


    

