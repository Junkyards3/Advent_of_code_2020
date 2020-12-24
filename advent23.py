#l = "389125467"
l = "538914762"

t = list(map(int,list(l)))
M = max(t)
m = min(t)
n = len(t)
curr_cup = 0

for i in range(100) :
	v = t[curr_cup]
	p = []
	for j in range(3) :
		if curr_cup == n-1-j :
			for k in range(3-j) :
				p.append(t.pop(0))
			curr_cup -= (3-j)
			break
		p.append(t.pop((curr_cup + 1)%(n-j)))
	dest = v-1
	while dest in p or dest < m :
		dest -= 1
		if dest < m :
			dest = M
	pos_dest = t.index(dest)
	t[pos_dest+1:pos_dest+1] = p
	curr_cup = (t.index(v)+1)%n
	
pos1 = t.index(1)
print("".join(map(str,t[pos1+1:] + t[:pos1])))
	
t = list(map(int,list(l)))
d = dict()
for i in range(len(t)-1) :
	d[t[i]] = t[i+1]
d[t[-1]] = max(t)+1
for i in range(max(t)+1,10**6) :
	d[i] = i+1
d[10**6] = t[0]
v = t[0]

for i in range(10**7) :
	sk = v
	p = []
	for j in range(3) :
		sk = d[sk]
		p.append(sk)
	sk = d[sk]
	dest = v-1
	while dest in p or dest < m :
		dest -= 1
		if dest < m :
			dest = 10**6
	d[p[2]] = d[dest]
	d[dest] = p[0]
	d[v] = sk 
	v = sk
	
print(d[1]*d[d[1]])