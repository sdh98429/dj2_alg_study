C = int(input())
F = list(map(int, input().split()))
F.sort()
print(F[0]*F[-1])