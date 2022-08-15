max_num = 0
num = 0
for _ in range(4):
  D, U = map(int, input().split())
  num += U - D
  if num > max_num:
    max_num = num
print(max_num)