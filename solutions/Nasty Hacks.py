n = int(input())
for i in range(n):
  a = input().split(' ')
  if int(a[0]) > int(a[1])-int(a[2]):
    print('do not advertise')
  elif int(a[0]) < int(a[1])-int(a[2]):
    print('advertise')
  else:
    print('does not matter')