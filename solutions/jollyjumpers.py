import sys
for i in sys.stdin:
	l = list(map(int, i.split()))
	n = l[0]
	s = set()
	j = True
	for i in range(1,n):
		d = abs(l[i] - l[i+1])
		if d in s or d > n-1:
			print('Not jolly')
			j = False
			break
		else:
			s.add(d)
	if j:
		print('Jolly')