# ! 피로도, dfs
# 87946

max_num = 0

def dfs(used, tired, dungeons):
    global max_num
    if sum(used) > max_num:
        max_num = sum(used)
    for i in range(len(dungeons)):
        if not used[i]:
            if tired >= dungeons[i][0]:
                used[i] = 1
                dfs(used, tired-dungeons[i][1], dungeons)
                used[i] = 0



def solution(k, dungeons):
    used = [False] * len(dungeons)
    dfs(used, k, dungeons)
    return max_num

# k	dungeons	result
# 80	[[80,20],[50,40],[30,10]]	3