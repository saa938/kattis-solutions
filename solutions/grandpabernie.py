N = int(input())
t = {}
for i in range(N):
	a,b=input().split()
	if a not in t:
		t[a] = []
	t[a].append(int(b))

for i,j in t.items():
	j.sort()

q = int(input())
for i in range(q):
	a,b = input().split()
	print(t[a][int(b)-1])