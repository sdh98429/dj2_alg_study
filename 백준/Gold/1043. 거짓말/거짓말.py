N, M = map(int, input().split())
T = list(map(int, input().split()))

parent = [i for i in range(N+1)]

def find(x):
  if x == parent[x]:
    return x
  else:
    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
  x = find(x)
  y = find(y)

  if x != y:
    parent[max(x, y)] = parent[min(x, y)]

P = []
for _ in range(M):
  P.append(list(map(int, input().split())))

for party_one in P:
  party_len = party_one[0]
  party_ind = party_one[1:]
  if party_len > 1:
    for ind in party_ind[1:]:
      union(party_ind[0], ind)

Parent_T = [find(parent[i]) for i in T[1:]]

tot = 0
for party_one in P:
  party_len = party_one[0]
  party_ind = party_one[1:]
  for ind in party_ind:
    if find(parent[ind]) in Parent_T:
      break
  else:
    if party_len:
      tot += 1

print(tot)