import sys
ab = []
for i in sys.stdin:
  ab.append(i.strip())
ab = ab[1:]
for i in range(len(ab)):
  if i%2==0:
    print(ab[i])