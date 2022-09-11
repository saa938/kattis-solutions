N = int(input())
l = list(map(int, input().split()))

d = {}
awk_lvl = N
for i in range(N):
	if l[i] not in d:
		d[l[i]] = i
	else:
		awk_lvl=min(awk_lvl, i-d[l[i]])
		d[l[i]]=i
print(awk_lvl)