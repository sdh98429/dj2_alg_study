# backtracking 부분수열의 합

def part_sum(ind, tot, length):
    global ans
    if ind == N:
        if tot == S and length:
            ans += 1
        return
    if nums[ind] > 0:
        if tot > S:
            return

    part_sum(ind+1, tot+nums[ind], length+1)
    part_sum(ind+1, tot, length)


N, S = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
part_sum(0, 0, 0)
print(ans)