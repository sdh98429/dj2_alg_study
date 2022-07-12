S = []
for _ in range(5):
    s = int(input())
    if s > 40:
      S.append(s)
    else:
      S.append(40)
AVG = sum(S)//5
print(AVG)