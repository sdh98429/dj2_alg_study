H, M, S = map(int, input().split())
Delay = int(input())
Last_S = H*60*60+M*60+S+Delay

print((Last_S//(60*60))%24, end=" ")
print((Last_S//60)%60, end=" ")
print(Last_S%60)
