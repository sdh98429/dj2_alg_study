N = int(input())
L = list(map(int, input().split()))
X = int(input())

L.sort()
start = 0
end = N-1
tot = 0

while start < end:
  if L[start] + L[end] > X:
    end -= 1
  elif L[start] + L[end] < X:
    start += 1
  else:
    tot += 1
    start += 1
print(tot)