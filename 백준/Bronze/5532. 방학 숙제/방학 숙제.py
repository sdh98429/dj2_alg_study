import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(min(L-math.ceil(A/C), L-math.ceil(B/D)))