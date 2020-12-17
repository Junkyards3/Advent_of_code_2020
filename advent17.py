neigh = [(i,j,k) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2)]
neigh.remove((0,0,0))

neigh2 = [(i,j,k,l) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) for l in range(-1,2)]
neigh2.remove((0,0,0,0))

def next_state(act) :
	global neigh
	act_n = []
	d = dict()
	for x,y,z in act :
		for i,j,k in neigh : 
			d[(x+i,y+j,z+k)] = d.setdefault((x+i,y+j,z+k),0) + 1
	for k,v in d.items() : 
		if v == 3 :
			act_n.append(k)
		elif v == 2 and k in act :
			act_n.append(k)
	return act_n

def next_state2(act) :
	global neigh2
	act_n = []
	d = dict()
	for x,y,z,w in act :
		for i,j,k,l in neigh2 : 
			d[(x+i,y+j,z+k,w+l)] = d.setdefault((x+i,y+j,z+k,w+l),0) + 1
	for k,v in d.items() : 
		if v == 3 :
			act_n.append(k)
		elif v == 2 and k in act :
			act_n.append(k)
	return act_n
	
f = open("input17.txt","r")
l = f.read()
f.close()
	
t = l.split("\n")
n = len(t)
active = []
for i in range(n) :
	for j in range(n) :
		if t[i][j] == "#" :
			active.append((i,j,0))

for k in range(6) : 
	active = next_state(active)
print(len(active))

active2 = []
for i in range(n) :
	for j in range(n) :
		if t[i][j] == "#" :
			active2.append((i,j,0,0))

for k in range(6) : 
	active2 = next_state2(active2)
print(len(active2))