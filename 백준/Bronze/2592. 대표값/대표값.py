from collections import Counter

L = []
for _ in range(10):
  L.append(int(input()))
print(sum(L)//10)
cnt = Counter(L)
print(cnt.most_common()[0][0])