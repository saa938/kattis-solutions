N = int(input())
l = []
for i in range(N):
	l.append(int(input().strip()))
l.sort(reverse=True)
# print(l)
price = 0
ii = 0
for i in range(N):
	if (i+1)% 3 == 0 and i != 0:
		price += l[i-2] + l[i-1]
		ii = i
		# print(l[i-2] , l[i-1])
# print(ii)
for j in range(ii+1, N):
	price += l[j]
print(price)