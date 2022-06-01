import sys
ab = []
for i in sys.stdin:
  ab.append(int(i.strip()))
x = ab[0]
n = ab[1] + 1
ab = ab[2:]
a = 0
for i in ab:
  a += i
print(x*n - a)