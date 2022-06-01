import sys
ab = []
for i in sys.stdin:
    ab.append(int(i.strip()))
l = []
for i in ab:
  if i % 42 not in l:
    l.append(i%42)
    

print(len(l))