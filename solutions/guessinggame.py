l={
	1:True,
	2:True,
	3:True,
	4:True,
	5:True,
	6:True,
	7:True,
	8:True,
	9:True,
	10:True
}
num = 1000000000
while num != 0:
	num = int(input().strip())
	if num == 0:
		break
	res = input().strip()
	if res == 'too high':
		for j in range(num,11):
			l[j] = False
	elif res == 'too low':
		for j in range(1,num+1):
			l[j] = False
	if res == 'right on':
		if l[num] == True:
			print("Stan may be honest")
		else: print("Stan is dishonest")
		l={
			1:True,
			2:True,
			3:True,
			4:True,
			5:True,
			6:True,
			7:True,
			8:True,
			9:True,
			10:True
		}