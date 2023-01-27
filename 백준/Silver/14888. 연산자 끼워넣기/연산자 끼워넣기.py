
def Calculator(idx, opr, num):
  global min_num, max_num
  if idx == N-1:
    if min_num > num:
      min_num = num
    if max_num < num:
      max_num = num
    return 
  plus, minus, multi, div = opr
  if opr[0]:
    Calculator(idx+1, [plus-1, minus, multi, div], num+A[idx+1])
  if opr[1]:
    Calculator(idx+1, [plus, minus-1, multi, div], num-A[idx+1])
  if opr[2]:
    Calculator(idx+1, [plus, minus, multi-1, div], num*A[idx+1])
  if opr[3]:
    if num >=0:
      Calculator(idx+1, [plus, minus, multi, div-1], num//A[idx+1])
    else:
      Calculator(idx+1, [plus, minus, multi, div-1], -(-num//A[idx+1]))
      

min_num = 987654321
max_num = -987654321

N = int(input())
A = list(map(int, input().split()))
Opr = list(map(int, input().split()))
Calculator(0, Opr, A[0])
print(max_num)
print(min_num)