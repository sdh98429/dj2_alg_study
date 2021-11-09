## stack !! 오큰수
# 오른쪽에서 왼쪽으로 이동해가며 스택을 쌓는다
# 스택의 top보다 큰 수가 나오면 top을 감소시키고, 아니라면 현재의 수를 스택 위에 쌓는다

N = int(input())
A = list(map(int, input().split()))


top = -1
s = [0] * (N+1)
ans = [-1] * N
for i in range(len(A)-1, -1, -1):
    while top >= 0:
        if A[i] >= s[top]:
            top -= 1
        else:
            ans[i] = s[top]
            top += 1
            s[top] = A[i]
            break
    else:
        top += 1
        s[top] = A[i]

print(*ans)


