a = input().strip()
b = [] 
for i in a:
  b.append(i)
c = set(b)
c = list(c)
if len(b)==len(c): print(1)
else: print(0)