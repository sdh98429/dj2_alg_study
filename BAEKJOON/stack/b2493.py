# greedy 탑
# 처음에 아주 큰 건물이 있다고 가정
# 스택에 건물을 순서대로 쌓으면서 만약 현재 건물의 스택 최상단의 건물보다 높다면,
# 스택의 건물을 빼주면서 바로 이전의 스택의 건물 위치를 저장해준다
# 참고로 높이가 같은 건물끼리는 수신하지 못한다
N = int(input())
tower = [0] + list(map(int, input().split()))
# 맨 왼쪽에 어마어마하게 큰 건물 가정
stack = [(0, 987654321)] + [0] * N
num = [0] * (N+1)

# 맨 왼쪽에 가상의 건물 넣었으니 0부터
top = 0

# 1번부터 시작
for i in range(1, N+1):
    # 스택이 비어 있지 않고, 스택의 건물이 현재 건물보다 낮으면
    while top != 0 and stack[top][1] <= tower[i]:
        # 스택의 건물 빼주고 바로 이전 스택 건물의 위치를 num에 저장
        num[stack[top][0]] = stack[top - 1][0]
        top -= 1
    # 스택에 위치와 높이 저장
    top += 1
    stack[top] = (i, tower[i])

# 스택에 남아있는 건물들은 높이가 낮아지는 순서
while top > 0:
    num[stack[top][0]] = stack[top-1][0]
    top -= 1

# 언패킹 사용해봄
print(*num[1:])

