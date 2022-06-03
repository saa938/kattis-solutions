a = input().strip()
a = a.split('()')
if len(a[0])==len(a[1]):
  print('correct')
else: print('fix')