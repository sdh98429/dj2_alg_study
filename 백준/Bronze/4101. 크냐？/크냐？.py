while True:
  A, B = map(int, input().split())
  if A or B:
    print("Yes" if A > B else "No")
  else:
    break