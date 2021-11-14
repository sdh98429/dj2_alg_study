# queue 앵무새 ! 말하지 않은 단어 있을 떄
N = int(input())
parrot = [[] for _ in range(N)]
for i in range(N):
    parrot[i] = list(input().split())
sentence = list(input().split())

for sen in sentence:
    error = 1
    for i in range(N):
        # 앵무새가 말하지 않은 단어가 남아있고, 그 단어가 현재 단어와 일치할 때
        if parrot[i] and sen == parrot[i][0]:
            parrot[i].pop(0)
            error = 0
    if error:
        break

if error:
    print('Impossible')
else:
    for i in range(N):
        # 앵무새가 말하지 않은 단어가 남아있을 때도 틀렸다
        if parrot[i]:
            print('Impossible')
            break
    else:
        print('Possible')
