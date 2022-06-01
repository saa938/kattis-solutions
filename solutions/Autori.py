a = input()
b = ''
for i in range(len(a)):
  if i == 0:
    b += a[i]
  if a[i]=='-':
    b += a[i+1]

print(b)