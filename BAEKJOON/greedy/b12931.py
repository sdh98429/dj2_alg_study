# 두 배 더하기
N = int(input())
B = list(map(int, input().split()))
# 1을 더하는 작업은 전부 따로 더해주고, 2를 곱하는 작업은 한 번에 모든 줄 적용 가능하니 최대값만 더해준다
one = 0 # 한 요소에 1을 더함
max_twice = 0 # 모든 요소에 2를 곱함
for b in B: # B 안의 요소 b
    twice = 0 # 두배
    while b: # b가 0이 아닐 떄
        if not b%2: # 2의 배수면
            b //= 2 # 2로 나눠줌
            twice += 1 # 2로 나눠준 횟수 추가
        else: # 2의 배수 아니면
            b -= 1 # 1을 빼줌
            one += 1 # 빼준 횟수 추가
    else: # b가 0일 때
        if max_twice < twice: # 현재 twice가 최대값보다 클 때 바꿔줌
            max_twice = twice

print(max_twice + one) # 2로 곱해준 최대값 + 1 더해준 모든 값