n,m=list(map(int, input().split()))
s = set(input().split())
l = []
for i in range(n-1):
	t = set(input().split())
	l.append(t)
ans = []
k = 0
for i in s:
	for j in l:
		if i not in j:
			break
	else:
		ans.append(i)
		k += 1

ans.sort()
print(k)
for i in ans:
	print(i)