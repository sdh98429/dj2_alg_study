import sys
input = sys.stdin.readline

N = int(input())

stack = [0] * (N+1)
ans = []
cnt = 0
top = -1

def push_s():
    global cnt, top, ans
    cnt += 1
    top += 1
    stack[top] = cnt
    ans.append('+')

def pop_s():
    global top, ans
    top -= 1
    ans.append('-')
    return stack[top+1]

push_s()
for _ in range(N):
    num = int(input())
    if cnt <= num:
        for _ in range(num-cnt):
            push_s()
        pop_s()
    elif num != pop_s():
        ans = ['NO']
        break

for a in ans:
    print(a)
