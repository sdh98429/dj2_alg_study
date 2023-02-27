def Pre(Root):
  print(chr(Root+65), end="")
  if BinaryTree[Root][0] != '.':
    Pre(ord(BinaryTree[Root][0])-65)
  if BinaryTree[Root][1] != '.':
    Pre(ord(BinaryTree[Root][1])-65)
  return

def In(Root):
  if BinaryTree[Root][0] != '.':
    In(ord(BinaryTree[Root][0])-65)
  print(chr(Root+65), end="")
  if BinaryTree[Root][1] != '.':
    In(ord(BinaryTree[Root][1])-65)
  return

def Post(Root):
  if BinaryTree[Root][0] != '.':
    Post(ord(BinaryTree[Root][0])-65)
  if BinaryTree[Root][1] != '.':
    Post(ord(BinaryTree[Root][1])-65)
  print(chr(Root+65), end="")
  return

N = int(input())
BinaryTree = [['.','.']] * N


for _ in range(N):
  Root, Left, Right = input().split()
  BinaryTree[ord(Root)-65] = [Left, Right]


Pre(0)
print()
In(0)
print()
Post(0)