import sys

for i in sys.stdin:
    ab = i.split()
    
c=0
for j in ab:
    j = int(j)
    if j<0:
        c+=1
print(c)