A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum(A) if sum(A) > sum(B) else sum(B))