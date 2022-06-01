import sys
ab = []
for i in sys.stdin:
  ab.append(int(i))
ab = ab[1:]
ab.reverse()

for i in ab:
  print(i)