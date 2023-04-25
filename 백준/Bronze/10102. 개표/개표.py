V = int(input())
S = input()
cnt_a = 0
for s in S:
  if s == 'A':
    cnt_a += 1
print('A' if cnt_a > V-cnt_a else ('Tie' if cnt_a == V-cnt_a else 'B'))