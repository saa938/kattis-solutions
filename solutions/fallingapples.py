rows, cols = list(map(int, input().split()))
l = []
for i in range(rows):
	string = input().strip()
	li = []
	for j in string:
		li.append(j)
	l.append(li)
obs = rows
for i in range(cols):
	obs=rows
	for j in range(rows-1,-1,-1):
		# print(i,j)
		if l[j][i]=='a':
			l[j][i]='.'
			l[obs-1][i]='a'
			obs -= 1
		elif l[j][i]=='#':
			obs=j
			
for i in range(rows):
	string = ''
	for j in range(cols):
		string += l[i][j]
	print(string)
# # 	string = ''