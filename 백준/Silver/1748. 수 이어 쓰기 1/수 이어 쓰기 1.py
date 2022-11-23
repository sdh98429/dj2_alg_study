N = input()
tot = 0

for i in range(len(N)-1):
  tot += (10**(i+1)-10**i)*(i+1)
tot += (int(N)-10**(len(N)-1)+1)*len(N)
print(tot)