t = []
f = open("input3.txt","r")
for l in f :
	t.append(list(map(lambda x: 1 if x == '#' else 0,l.replace("\n",""))))
f.close()

nb_trees = 0
c = 0
n = len(t[1])
for line in t :
	nb_trees += line[c]
	c = (c+3)%n
print(nb_trees)

m = len(t)
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
nb_tree_list = []
for slope in slopes : 
	nb_trees = 0
	r = slope[0]
	d = slope[1]
	l = 0
	c = 0
	while l < m :
		nb_trees += t[l][c]
		c = (c+r)%n
		l = (l+d)
	nb_tree_list.append(nb_trees)

print(nb_tree_list)
v = 1
for a in nb_tree_list :
	v *= a
print(v)