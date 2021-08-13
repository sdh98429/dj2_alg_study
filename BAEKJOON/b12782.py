T = int(input())


for tc in range(1, T+1):
    P = input().split()
    exclusive = int(P[0],2)^int(P[1],2)
    tot_num = sum(map(int,str(bin(exclusive))[2:]))
    ones = exclusive & int(P[0],2)
    ones_num = sum(map(int,str(bin(ones))[2:]))
    if ones_num > tot_num - ones_num:
        print(ones_num)
    else:
        print(tot_num - ones_num)

