ab = input().strip().split(' ')
ab = ab[:-1]
ac = input().strip().split(' ')
g = int(ab[0])
t = int(ab[1])
g = (g-t)*90/100
i = 0
for j in ac:
  i += int(j)
print(int(g-i))