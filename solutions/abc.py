a,b,c = sorted(input().split())
order = input().strip()
ans = ''
for i in order:
	if i == 'C':
		ans += c +' '
	elif i == 'B':
		ans += b+' '
	else: ans += a+' '
print(ans)