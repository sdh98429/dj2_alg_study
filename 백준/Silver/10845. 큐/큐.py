import sys

N = int(sys.stdin.readline())
queue = []

class ListQueue(object):
  def __init__(self):
    self.queue = []

  def enqueue(self, num):
    self.queue.append(num)

  def dequeue(self):
    if not self.queue:
      print(-1)
    else:
      print(self.queue[0])
      self.queue.pop(0)

  def sizeQueue(self):
    print(len(self.queue))

  def emptyQueue(self):
    if not self.queue:
      print(1)
    else:
      print(0)
  
  def frontQueue(self):
    if not self.queue:
      print(-1)
    else:
      print(self.queue[0])

  def backQueue(self):
    if not self.queue:
      print(-1)
    else:
      print(self.queue[-1])

lq = ListQueue()

for _ in range(N):
  command = sys.stdin.readline().split()
  if command[0] == 'push':
    lq.enqueue(command[1])
  elif command[0] == 'pop':
    lq.dequeue()
  elif command[0] == 'size':
    lq.sizeQueue()
  elif command[0] == 'empty':
    lq.emptyQueue()
  elif command[0] == 'front':
    lq.frontQueue()
  elif command[0] == 'back':
    lq.backQueue()
  