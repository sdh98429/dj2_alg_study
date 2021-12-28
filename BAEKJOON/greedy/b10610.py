# greedy 30
# 배수 조건

N = list(map(int, input()))
N.sort(reverse=True)

print(-1) if N[-1] or sum(N)%3 else print(''.join(map(str, N)))



# 기존의 좀 더 긴 코드
# import sys
# N = sorted(list(map(int, list(sys.stdin.readline().rstrip()))), reverse=True)
#
#
# if not N[-1] and  not sum(N)%3: # 10의 배수 0 있고 합이 3의 배수
#     for n in N:
#         print(n, end="")
# else:
#     print(-1)