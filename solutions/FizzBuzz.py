import sys

for i in sys.stdin:
    ab = i.split()
a = int(ab[0])
b = int(ab[1])
c = int(ab[2])

for i in range(1,c+1):
  if i%a==0 and i%b==0:
    print('FizzBuzz')
  elif i%a==0:
    print('Fizz')
  elif i%b == 0: print('Buzz')
  else: print(i)
    