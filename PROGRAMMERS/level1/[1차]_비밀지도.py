# [1차] 비밀지도
# 17681

def solution(n, arr1, arr2):
    answer = []
    arr = []
    for i in range(n):
        arr.append(arr1[i] | arr2[i])
    print(arr)
    for a in arr:
        row = ''
        for i in range(n):
            if a%2:
                row = '#' + row
            else:
                row = ' ' + row
            a //= 2
        answer.append(row)
    return answer

# 매개변수	값
# n	5
# arr1	[9, 20, 28, 18, 11]
# arr2	[30, 1, 21, 17, 28]
# 출력	["#####","# # #", "### #", "# ##", "#####"]
# 매개변수	값
# n	6
# arr1	[46, 33, 33 ,22, 31, 50]
# arr2	[27 ,56, 19, 14, 14, 10]
# 출력	["######", "### #", "## ##", " #### ", " #####", "### # "]