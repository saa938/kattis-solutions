import sys
d = {}
k={}
for i in sys.stdin:
	ans = i.strip()[5:len(i)-1]
	l = i.split()
	if l[0] == 'def':
		if l[1] in d:
			k.pop(d[l[1]])
		d[l[1]] = int(l[2])
		k[int(l[2])] = l[1]
	elif l[0] == 'calc':
		sum = ''
		for j in l[1:-1]:
			if j in d:
				sum += str(d[j])
			elif j == "+" or j == "-":
				sum += j
			else:
				print(ans, "unknown")
				break
		else:
			asdasd = eval(sum)
			if asdasd in k:
				print(ans, k[eval(sum)])
			else:
				print(ans, 'unknown')
	if l[0] == 'clear':
		d= {}
		k={}