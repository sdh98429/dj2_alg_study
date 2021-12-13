# queue ! 트럭
# 다리 크기 만큼 큐를 만들어 총 무게 넘치지 않을 때만 새로운 트럭 받아들이기
# 마지막엔 다리 크기 만큼 시간 추가
# 다리 기준 말고 트럭 기준으로도 풀 수 있을 듯
from collections import deque
n, w, L = map(int, input().split())
A = list(map(int, input().split()))

q = deque()
done = 0 # 새로 들어갈 트럭 번호
wgt = 0 # 다리 위의 무게
time = 0 # 소요 시간
for i in range(w): # 일단 다리를 0의 무게 가지는 트럭으로 채우자
    q.append(0)
while done < n: # 아직 트럭이 전부 다리 위에 안 올라갔을 때
    wgt -= q.popleft() # 다리 맨 왼쪽의 트럭부터 뺀다
    if wgt + A[done] <= L: # 새로운 트럭이 올라갈 수 있다면 트럭 추가 및 무게 추가
        q.append(A[done])
        wgt += A[done]
        done += 1

    else:
        q.append(0)

    time += 1 # 시간 1흐름

time += w # 새로 들어온 트럭이 다리 끝으로 나오기
print(time)


