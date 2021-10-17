# greedy 멀티탭 스케줄링
# 플러그가 비어있으면 다 꽂고,
# 새로 꽂아야하는 경우 가장 나중에 쓰게 될 전기플러그를 뺸다

N, K = map(int, input().split())
E = list(map(int, input().split()))

# 플러그의 상태
plug = []
# 뺀 횟수
cnt = 0
for i in range(K):
    # 현재 전기용품이 플러그에 없을 때
    if E[i] not in plug:
        # 플러그가 비어있으면 바로 꽂음
        if len(plug) < N:
            plug.append(E[i])
        else:
            # 가장 나중에 뽑는 전기용품 번호 max_p, 그리고 뽑는 차례 max_order
            max_order = 0
            max_p = plug[0]
            # 현재 꽂혀있는 전기용품 모두
            for p in plug:
                # 이후에 언제 사용할지
                for n in range(i+1, K):
                    # 가장 먼저 만나는 차례 기록
                    if E[n] == p:
                        if n > max_order:
                            max_order = n
                            max_p = p
                        break
                # 만약 한 번도 안쓴다면 최대값 부여
                else:
                    max_order = 987654321
                    max_p = p
            # 뽑고 새로 꽂으며 횟수 추가
            plug.remove(max_p)
            plug.append(E[i])
            cnt += 1
print(cnt)