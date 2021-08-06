T = int(input())

err = 0
tot1 = 0
tot2 = 0
tot3 = 0
while T:
    if not T%300:
        T -= 300
        tot1 += 1
    else:
        if not T%60:
            T -= 60
            tot2 += 1
        else:
            if not T%10:
                T -= 10
                tot3 += 1
            else: 
                err = 1
                break
if err:
    print(-1)
else:    
    print(f'{tot1} {tot2} {tot3}')