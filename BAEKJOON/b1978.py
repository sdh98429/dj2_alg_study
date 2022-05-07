# 소수 찾기

def isPrime(p):
    if p >= 2:
        for i in range(2, int(p**(1/2)+1)):
            if not p%i:
                break
        else:
            return True
    return False

N = int(input())
P = map(int, input().split())

ans = 0
for p in P:
    if isPrime(p):
        ans += 1
print(ans)