import sys
ab = []
for i in sys.stdin:
    ab.append(i.split())

print(ab[0][1])