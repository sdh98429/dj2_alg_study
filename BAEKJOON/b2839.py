T = int(input())

tot=0
while T:
    if T%5==0:
        T -= 5
        tot += 1
    else:
        T -= 3
        tot += 1
    if T < 0:
        tot = -1
        break
print(tot)