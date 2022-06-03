n = int(input())
for i in range(n):
  ab = input().split(' ')
  bpm = 60*int(ab[0])/float(ab[1])
  diff = 60/float(ab[1])
  mini = bpm - diff
  maxi = bpm + diff
  print("{} {} {}".format(round(mini, 4),round(bpm, 4),round(maxi, 4)))
