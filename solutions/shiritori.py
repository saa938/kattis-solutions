N = int(input())
s = set()
prev = input().strip()
s.add(prev)
bool = False
for i in range(N-1):
	string = input().strip()
	if string[0] != prev[-1] or string in s:
		if i % 2 == 0:
			print("Player 2 lost")
		else: print("Player 1 lost")
		bool = True
		break
	s.add(string)
	prev = string
if bool == False:
	print('Fair Game')