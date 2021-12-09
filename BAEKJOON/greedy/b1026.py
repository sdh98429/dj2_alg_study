# greedy 보물
# 곱의 합이 최소가 되기 위해서는 A에서 가장 큰 수와 B에서 가장 큰 수를 매칭해준다
# A와 B의 크기 순서를 반대로 하여 각각 곱해준다

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A[i] * B[i]

print(ans)