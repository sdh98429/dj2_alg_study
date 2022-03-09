# 하샤드 수
# 12947

def solution(x):
    return True if not x%(sum(map(int, list(str(x))))) else False

# arr	return
# 10	true
# 12	true
# 11	false
# 13	false