import math

N, K = map(int, input().split())
print(math.factorial(N-1)//(math.factorial(N-K)*math.factorial(K-1)))