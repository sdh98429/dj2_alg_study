N = int(input())
if N%8 in [1]:
  print(1)
elif N%8 in [0, 2]:
  print(2)
elif N%8 in [3, 7]:
  print(3)
elif N%8 in [4, 6]:
  print(4)
elif N%8 in [5]:
  print(5)
