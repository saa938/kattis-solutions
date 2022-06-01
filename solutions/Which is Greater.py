import sys

for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])

if a>b:
  print(1)
else: print(0)