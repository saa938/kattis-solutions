import sys

for i in sys.stdin:
  l = i.split()

for i in range(len(l)):
  l[i] = int(l[i])

l.sort()
 
string = ''
a = 0
b = 1
c = 0

while b <= len(l) and a < len(l):
  if b < len(l) and l[b-1] + 1 == l[b]:
    b += 1
    c += 1
  elif c >= 2:
    string += str(l[a]) + '-'+str(l[b-1])+' '
    c = 0
    a = b
    b += 1
  elif c == 1:
    string += str(l[b-2]) + ' ' + str(l[b-1]) + ' '      
    a = b
    b += 1
    c = 0
  else:
    string += str(l[a]) + ' '
    a += 1
    b = a + 1
    c= 0

print(string)