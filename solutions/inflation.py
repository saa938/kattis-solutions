n = int(input())
l = []
for i in range(n, 0, -1):
	l.append(i)
canisters = sorted(list(map(int, input().split())), reverse=True)

f = 1
for i in range(n):
	d = canisters[i] / l[i]
	if d > 1:
		print('impossible')
		break
	if d == 0:
		print('0')
		break
	f = min(d,f)
else:
	print(f)