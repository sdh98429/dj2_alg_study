# !! 땅따먹기, dp 사용
# 12913

def solution(land):
    dp = [[0] * 4 for _ in range(len(land))] # 각 열을 선택했을 때 최대값 저장 dp
    dp[0] = (land[0]) # 첫번째 초기값
    
    for i in range(1, len(land)): # 각 행에 대하여
        for j in range(4): # j번 열 선택시 최대값
            max_score = 0 # j번 열 최대값
            for d in range(4): # 바로 전 행에서 선택도니 열
                if d != j and max_score <= land[i][j] + dp[i-1][d]: # 열이 겹치지 않고 최대값 갱신
                    max_score = land[i][j] + dp[i-1][d]
            dp[i][j] = max_score

    return max(dp[-1]) # 마지막 행의 최대값

# land	answer
# [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16