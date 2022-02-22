# !! 행렬 테두리 회전하기, deepcopy 속도 느림
# 77485

# import copy

def deep_copy(rows, columns, matrix): # deep copy 대체, 속도 더 빠름
    new_matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            new_matrix[i][j] = matrix[i][j]
    
    return new_matrix

def solution(rows, columns, queries):
    answer = []
    
    matrix = [[0] * columns for _ in range(rows)] # 회전 전의 행렬
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i*columns+(j+1)

    for q in queries:
        small = 987654321 # 가능한 최소값
        # new_matrix = copy.deepcopy(matrix) # copy.deepcopy
        new_matrix = deep_copy(rows, columns, matrix) # 회전 이후 정보 저장할 new_matrix
        for i in range(q[0]-1, q[2]-1): # 왼쪽, 오른쪽 열
            new_matrix[i+1][q[3]-1] = matrix[i][q[3]-1] # 오른쪽 열 이동
            small = small if small < matrix[i][q[3]-1] else matrix[i][q[3]-1] # 최소 값 찾기
            new_matrix[i][q[1]-1] = matrix[i+1][q[1]-1] # 왼쪽 열 이동
            small = small if small < matrix[i+1][q[1]-1] else matrix[i+1][q[1]-1]

        for j in range(q[1]-1, q[3]-1): # 위, 아래 행
            new_matrix[q[0]-1][j+1] = matrix[q[0]-1][j] # 위 행 이동
            small = small if small < matrix[q[0]-1][j] else matrix[q[0]-1][j]
            new_matrix[q[2]-1][j] = matrix[q[2]-1][j+1] # 아래 행 이동
            small = small if small < matrix[q[2]-1][j+1] else matrix[q[2]-1][j+1]
        
        answer.append(small) # 최소 값 더하기
        matrix = new_matrix # 회전 이후의 행렬을 matrix로
        
    return answer

# rows	columns	queries	result
# 6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
# 3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
# 100	97	[[1,1,100,97]]	[1]

