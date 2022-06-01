import sys

for i in sys.stdin:
    ab = int(i)

if ab%2==0: print('Bob')
else: print('Alice')