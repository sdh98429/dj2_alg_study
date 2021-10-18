# stack 옥상 정원 꾸미기
# 새로 들어오는 건물의 높이와 비교
import sys
input = sys.stdin.readline

N = int(input())
H = [int(input()) for _ in range(N)]
stack = [0] * (N+1)

top = -1
tot = 0 # 건물 합
for i in range(N):
    while top != -1 and stack[top][1] <= H[i]: # 만약 스택이 비어있지 않고 새 건물이 stack의 건물 이상이라면
        tot += i - stack[top][0] -1 # 스택 건물과 새 건물의 거리만큼 더해줌
        top -= 1
    top += 1 # 아니라면 인덱스와 높이 스택에 쌓기
    stack[top] = (i, H[i])

# 까다로웠던 부분
# stack이 아직 남아있다면, 각각 남아있는 건물로부터 우측 끝(N-1)까지의 거리만큼 건물을 더 볼 수 있다
while top != -1:
    tot += N-1 - stack[top][0]
    top -= 1

print(tot)
