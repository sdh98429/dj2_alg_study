# queue !! 프린터 큐
# 존재하는 모든 중요도를 MAX에 넣어주고,
# MAX에서 제일 큰 값부터 세어주기 시작한다.
# 그리고 다시 썼던 used에 돌아오면, 마지막으로 만났던 used를 저장했던 tmp 값으로 돌아온다.
# tmp로 돌아오는 과정이 중요한 이유는 마지막으로 사용했던 used와 시작할 때 사용했던 used 사이에,
# 다음 max_num이 존재할 수도 있기 때문이다.
# 아래 주석처리된 코드는 해당하는 오류와 반례를 보여준다.
# 그런데 주호님 코드가 훨씬 좋은듯...

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    book = list(map(int, input().split()))
    MAX = [] # 중요도의 종류
    for b in book:
        if b not in MAX:
            MAX.append(b)
    MAX.sort() # 중요도 오름차 순 정렬
    used = [0] * N # 사용했는지 여부 확인
    cnt = 0
    i = 0
    m = -1
    max_num = MAX[-1]
    while True:
        if book[i] == MAX[m]: # 만약 남은 책 중 중요도 최대라면
            if not used[i]: # 사용 안했다면 tmp에 현재 i 저장하고 cnt 갯수 올림
                cnt += 1
                used[i] = 1
                tmp = i
                if i == M: # M을 찾으면 끝
                    print(cnt)
                    break
            else:
                m -= 1 # 만약 한바퀴 돌아온거라면 다음 중요도 찾고, 바로 이전 tmp로 돌아감
                i = tmp
        i = (i + 1)%N # 순환할수 있게 %N


# tmp 없어서 틀린 코드와 반례
# 1
# 38 29
# 7 1 8 4 7 1 3 4 6 5 7 8 3 2 8 5 9 4 6 8 2 1 8 7 4 8 5 3 7 6 3 4 6 1 5 2 8 5

# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     book = list(map(int, input().split()))
#     MAX = []
#     for b in book:
#         if b not in MAX:
#             MAX.append(b)
#     MAX.sort()
#     used = [0] * N
#     cnt = 0
#     i = 0
#     m = -1
#     print(MAX)
#     max_num = MAX[-1]
#     while True:
#         if book[i] == MAX[m]:
#             if not used[i]:
#                 cnt += 1
#                 used[i] = 1
#                 if i == M:
#                     print(cnt)
#                     break
#             else:
#                 m -= 1
#         i = (i + 1)%N

# 보고 배워야하는 주호님 코드
for _ in range(int(input())):
    N, M = map(int, input().split())
    check = [0] * N
    check[M] = True
    nums = list(map(int, input().split()))

    cnt = 1
    while nums:
        idx = nums.index(max(nums))
        if check[idx]:
            break

        nums = nums[idx + 1 :] + nums[: idx]
        check = check[idx + 1 :] + check[: idx]
        cnt += 1

    print(cnt)




