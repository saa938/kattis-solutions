cost = float(input())
total = 0
for i in range(int(input())):
  a = input().strip().split(' ')
  total += float(a[0])*float(a[1])*cost
print(format(round(total, 6)))