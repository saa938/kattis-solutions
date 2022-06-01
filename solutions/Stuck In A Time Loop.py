import sys

for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])

for i in range(1,a+1):
    print(i, "Abracadabra")