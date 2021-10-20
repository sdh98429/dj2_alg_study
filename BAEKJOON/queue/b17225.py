# 세훈이의 선물가게
# 먼저 B와 R의 선물 큐를 나눈다
# 각 손님의 선물 포장 끝나는 시간 기준으로, 다음 선물이 끝나는 시간보다 빨리 들어오면 끝나는 시간을 큐의 마지막에 넣고
# 만약 끝나는 시간보다 다음 선물이 늦게 들어오면 큐의 마지막을 다음 선물이 들어오는 시간으로 바꾼다
# 그리고 B와 R의 선물 큐의 맨 앞을 비교해주며 더 작은 값의 큐를 deque하며 번호를 매긴다

# 다이어트 코드, 설명은 주석처리된 코드를 봐주세요

import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())
q = [[987654321] * 100 * (N+1), [987654321] * 100 * (N+1)]

front = [0, 0]
rear = [-1, -1]

for _ in range(N):
    t, c, m = input().split()
    t = int(t)
    m = int(m)
    if c == 'R':
        p = 1
    else:
        p = 0
    if rear[p] == -1:
        rear[p] += 1
        q[p][rear[p]] = t
    if q[p][rear[p]] < t:
        q[p][rear[p]] = t
    while m:
        rear[p] += 1
        q[p][rear[p]] = q[p][rear[p]-1] + (B if p else A)
        m -= 1

q[0][rear[0]] = 987654321
q[1][rear[1]] = 987654321

box = 0
while front[0] != rear[0] or front[1] != rear[1]:
    box += 1
    p = 1
    if q[0][front[0]] <= q[1][front[1]]:
        p = 0
    q[p][front[p]] = box
    front[p] += 1

for i in (0, 1):
    print(rear[i])
    print(*q[i][:rear[i]])

#####
## 살 빼기 전 코드 주석처리 풀어주세요

# import sys
# input = sys.stdin.readline
#
#
# A, B, N = map(int, input().split())
# qr = [987654321] * 100 * (N+1) # R의 포장 시간 큐, 987654321로 가장 늦게 끝나는 시간으로 초기화
# qb = [987654321] * 100 * (N+1) # B의 포장 시간 큐
# ansr = [0] * 100 * (N+1) # R의 선물 번호 큐
# ansb = [0] * 100 * (N+1) # B의 선물 번호 큐
#
# frontr = 0 # qr용 front, rear
# rearr = -1
# frontb = 0 # qb용 front, rear
# rearb = -1
#
# for _ in range(N):
#     t, c, m = input().split()
#     t = int(t)
#     m = int(m)
#     if c == 'R': # 색깔이 R이라면
#         if rearr == -1: # 큐가 비어있다면 현재 선물 포장 시작 시간 추가
#             rearr += 1
#             qr[rearr] = t
#         if qr[rearr] < t: # 만약 현재 선물이 들어온게 이전 선물 마지막 포장 시간 보다 느리면 큐 마지막을 현재 선물 시간으로 바꿈
#             qr[rearr] = t
#         while m: # 선물 남아있다면 큐에 포장 시작 시간 + B만큼 넣어서 선물 포장이 끝나는 시간까지 큐에 넣어줌
#             rearr += 1
#             qr[rearr] = qr[rearr-1] + B
#             m -= 1
#     else:
#         # 색깔이 B일 떄도 동일
#         if rearb == -1:
#             rearb += 1
#             qb[rearb] = t
#         if qb[rearb] < t:
#             qb[rearb] = t
#         while m:
#             rearb += 1
#             qb[rearb] = qb[rearb-1] + A
#             m -= 1
# # B, R에서 마지막 손님의 마지막 선물 포장이 끝나는 시간은 없앤다
# qb[rearb] = 987654321
# qr[rearr] = 987654321
#
#
# box = 0 # 선물 번호
# while frontb != rearb or frontr != rearr: # B에도 선물 남아있고 R에도 선물 남아있다면
#     box += 1
#     # 만약 B가 R 포장 시간보다 빠르거나 같다면 B를 큐에서 꺼내줌
#     if qb[frontb] <= qr[frontr]:
#         ansb[frontb] = box
#         frontb += 1
#     # 아니라면 R을 꺼내줌
#     else:
#         ansr[frontr] = box
#         frontr += 1
#
# # 선물의 개수와 언패킹을 이용한 선물 번호
# print(rearb)
# print(*ansb[:rearb])
# print(rearr)
# print(*ansr[:rearr])