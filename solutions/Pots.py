import sys
ab = []
for i in sys.stdin:
  ab.append(int(i.strip()))
ab = ab[1:]
c = 0
for i in ab:
  x = i%10
  i //= 10
  c += i**x
print(c)