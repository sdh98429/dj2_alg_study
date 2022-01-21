# ! 소수 만들기
# 12977

cand = []

def dfs(idx, cnt, tot, nums): # 원소의 개수가 총 3인 조합 완성
    if cnt == 3:
        cand.append(tot)
        return

    if idx == len(nums):
        return

    dfs(idx + 1, cnt + 1, tot + nums[idx], nums)
    dfs(idx + 1, cnt, tot, nums)


def solution(nums):
    answer = 0

    dfs(0, 0, 0, nums)
    for c in cand:
        for i in range(2, int(c ** 1 / 2) + 1): # 소수인지 제곱근까지 확인
            if not c % i: # 만약 나눠진다면
                break
        else: # 끝까지 안나눠진다면
            answer += 1

    return answer

# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4