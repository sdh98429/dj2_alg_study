temp = 'start'
while True:
  A = float(input())
  if A == 999:
    break
  else:
    if temp != 'start':
      num1 = A - temp
      print(f"{num1:.2f}")
    temp = A