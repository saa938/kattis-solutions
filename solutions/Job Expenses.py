n = input()
ab = input().strip().split()
c = 0
for i in ab:
  if int(i)<0:
    c += int(i)
print(abs(c))