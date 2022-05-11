# 최대공약수와 최소공배수, 유클리드 호제법

def gcd(a, b): # 최대공약수
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b): # 최소공배수
    return int(a * b / gcd(a, b))

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))