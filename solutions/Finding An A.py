import sys

for i in sys.stdin:
  ab = str(i.strip())
a = []
for i in ab:
  a.append(i)
c = 0
b = ''
for i in a:
  if c == 0 and i == 'a':
    c = 1
  if c == 1:
    b += i

print(b)