import sys

for i in sys.stdin:
    ab=int(i.strip())

def otherBasesToBaseTen(num, base):
  num = str(num)
  newnum = ""
  ans = 0
  for i in range(len(num)):
    newnum += num[-(i+1)]
  for i in range(len(str(newnum))):
    ans += (base**i * int(newnum[i]))
  return ans
def BaseTenToOtherBases(num, newbase):
  ans = 0
  power = 0
  while newbase**power <= num:
    power+=1
  power-=1
  while num != 0:
    while num - newbase**power >= 0:
      ans += 10**power
      num -= newbase**power
    power-=1
  return ans

ab = BaseTenToOtherBases(ab, 2)
ab = str(ab)
ab = ab[::-1]
ab = int(ab)
print(otherBasesToBaseTen(ab, 2))