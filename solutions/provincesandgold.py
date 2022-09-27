g,s,c = list(map(int, input().split()))
buy_pow = g*3 + s*2+c
ans1 = ''
ans2 = ''
vp = {
	'Province': 8,
	'Duchy' : 5,
	'Estate' : 2
}
tc = {
	'Gold': 6,
	'Silver': 3,
	'Copper': 0
}
for i,j in vp.items():
	if buy_pow >= j:
		ans1 = i+' or '
		break
for i,j in tc.items():
	if buy_pow >= j:
		ans2 = i
		break
print(ans1 +ans2)