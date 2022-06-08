a = input().strip()
b = input().strip()
s = 1
for i in range(len(a)):
  if a[i]!=b[i]:
    s *= 2
print(s)