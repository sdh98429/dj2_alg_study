# def oper2(A,B):
#     max_act = -1
#     min_act = -1
#     div = B//A
#     while div:
#         div //= 2
#         max_act += 1

#     for i in range(1<<max_act):
#         a = A
#         for j in range(max_act):
#             if i & (1<<j):
#                 a = 10 * a + 1
#             else:
#                 a *= 2
#             if B == a:
#                 return(j+2)
#             elif B < a:
#                 break
#     else:
#         return(-1)

# A, B = list(map(int, input().split()))
# print(oper2(A,B))
# 비트 연산자로 풀면 1, 1000000000 시간 초과됨

def oper(A,B):
    result = 1 # 연산 횟수
    while B > A: # B가 A보다 감소했을때 불필요한 계산 안하도록
        if B%10 == 1: # 맨 오른쪽이 1
            B = (B-1)//10 # 1을 수의 가장 오른쪽에 추가하는 연산 역으로
            result += 1
        elif not B%2: # 2로 나누어지는 경우
            B //= 2
            result += 1
        else: # 더이상 역으로 연산할 수 없으므로 -1
            return(-1)
        if B == A: # B와 A가 같아짐
            return(result)
    return(-1) #B가 A보다 작아졌으면 불가능

A, B = list(map(int, input().split()))
print(oper(A,B))