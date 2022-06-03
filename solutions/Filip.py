a = input().split()
b = a[0]
b = b[::-1]
c = a[1]
c = c[::-1]
print(max(int(b),int(c)))