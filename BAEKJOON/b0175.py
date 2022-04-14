# 나누기
N = input()
F = int(input())

for i in range(100):
    if not (int(N[:-2]) * 100 + i)%int(F):
        print(i) if i >= 10 else print('0' + str(i))
        break