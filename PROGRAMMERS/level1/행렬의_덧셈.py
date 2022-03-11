# 행렬의 덧셈
# 12950

def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer

# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]