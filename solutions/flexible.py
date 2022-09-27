l=[0]
w,p=list(map(int, input().split()))
p += 2
l += list(map(int, input().split()))
l.append(w)

s = set()
for i in range(p):
	for j in range(i):
		s.add(l[i]-l[j])
s = sorted(list(s))
ans = ''
for i in s:
	ans += str(i) + ' '
print(ans)