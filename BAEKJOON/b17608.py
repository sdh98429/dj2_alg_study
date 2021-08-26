import sys
input = sys.stdin.readline

N = int(input())

sticks = [int(input()) for _ in range(N)]

max_s = 0
result = 0
for stick in sticks[::-1]:
    if stick > max_s:
        max_s = stick
        result += 1
print(result)