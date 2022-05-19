# ! 단어 정렬, sorted 람다식 다중 정렬

N = int(input())
L = []
for _ in range(N):
    i = input()
    if i not in L:
        L.append(i)

fL = sorted(L, key=lambda x: (len(x), x)) # 다중 정렬, 람다식의 첫번째로 정렬 후 같은 순서면 두번째 요소로 정렬한다
print(*fL, sep='\n')