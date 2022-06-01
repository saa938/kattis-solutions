import sys
ab = []
for i in sys.stdin:
  ab.append(i)
ab = ab[1:]
x = 0
for i in ab:
  i = i.split(' ')
  x += float(i[0])*float(i[1])
print(x)