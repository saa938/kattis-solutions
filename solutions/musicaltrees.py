N,M=list(map(int, input().split()))
people=sorted(list(map(int,input().split())))
trees = sorted(list(map(int, input().split())))

def iscloser(t, c, p):
	if abs(p-t) < abs(p-c):
		return t
	return c  
	
picked_trees = set()
ans = 0

for i in range(N):
	person = people[i]
	closest_tree=100000
	
	for j in range(M):
		tree=trees[j]
		closest_tree=iscloser(tree, closest_tree, person)
		
	if closest_tree in picked_trees:
		ans += 1
	else:
		picked_trees.add(closest_tree)

print(ans)