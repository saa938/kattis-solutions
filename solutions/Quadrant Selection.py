import sys
ab = []
for i in sys.stdin:
    ab.append(i.strip())
x = int(ab[0])
y = int(ab[1])

if x>0 and y>0:
  print(1)
elif x<0 and y>0:
  print(2)
elif x<0 and y<0:
  print(3)
else: print(4)