N, B = input().split()

ans = 0
for i in range(len(N)):
  ans += (int(N[len(N)-1-i]) * (int(B) ** i) if (ord(N[len(N)-1-i]) < 65) else (ord(N[len(N)-1-i])-55) * (int(B) ** i))
print(ans)