n = int(input())
for i in range(n):
  a = input().strip().split(' ')
  sum = 0
  for i in range(1, len(a)):
    sum+=int(a[i])
  sum-=int(a[0])-1
  print(sum)