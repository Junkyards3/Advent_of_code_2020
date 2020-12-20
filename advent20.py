import math
import copy
def tr(tile,r,s) :
	k = len(tile)
	ctile = [[None]*k for i in range(k)]
	for i in range(k) :
		for j in range(k) :
			if r == 0 :
				ctile[i][j] = tile[i][j]
			if r == 1 :
				ctile[i][j] = tile[k-1-j][i]
			if r == 2 :
				ctile[i][j] = tile[k-1-i][k-1-j]
			if r == 3 :
				ctile[i][j] = tile[j][k-1-i]
	if s == 1 :
		ctile.reverse()
	return ctile

def stick(t1,r1,s1,t2,r2,s2,side) :
	ct1 = tr(t1,r1,s1)
	ct2 = tr(t2,r2,s2)
	k = len(t1)
	if side == "UP" :
		for i in range(k) :
			if ct1[k-1][i] != ct2[0][i] :
				return False
		return True 
	else :
		for j in range(k) :
			if ct1[j][k-1] != ct2[j][0] :
				return False
		return True
		
def pprint(tile) :
	s = "\n".join(list(map(lambda x:"".join(x),tile)))
	print(s)
	
def pprintt(t) :
	s = ""
	for i in range(len(t)) :
		for j in range(len(t)) :
			if t[i][j] :
				s += str(t[i][j][0])
			else :
				s += "None"
			s += " "
		s += "\n"
	print(s)
	
def get_choices(t,c1,c2,r_ids,d) :
	ret = []
	for id in r_ids :
		for r in range(4) :
			for s in range(2):
				b1 = (c1 == 0)
				if not b1 :
					idu,tileu,ru,su = t[c1-1][c2]
					b1 = stick(tileu,ru,su,d[id],r,s,"UP")
				b2 = (c2 == 0)
				if not b2 :
					idu,tileu,ru,su = t[c1][c2-1]
					b2 = stick(tileu,ru,su,d[id],r,s,"LEFT")
				if b1 and b2 :
					ret.append((id,d[id],r,s))
	return ret

def find_sm(fp) :
	p = copy.deepcopy(fp)
	seam = "                  # " + "" +"#    ##    ##    ###" + "" + " #  #  #  #  #  #   "
	seamp = []
	n = 0
	for i in range(3) :
		for j in range(20) :
			if seam[20*i+j] == "#" :
				seamp.append((i,j))
	for i in range(len(p)-3) :
		for j in range(len(p)-20):
			cond = True
			for x,y in seamp :
				if p[i+x][y+j] == "." :
					cond = False 
					break 
			if cond :
				n += 1
				for x,y in seamp :
					p[i+x][y+j] = "."
	return n
	
f = open("input20.txt","r")
l = f.read()
f.close()
	
d = dict()
tx = l.split("\n\n")

for tile in tx :
	tile2 = tile.split("\n")
	id = int(tile2[0].split(" ")[1][:-1])
	ttile  = list(map(list,tile2[1:]))
	d[id] = ttile 
	
Ns = int(math.sqrt(len(d)))
N = Ns*Ns
t = [[None]*Ns for i in range(Ns)]
c = 0
dict_choices = [[]]*N
is_going_up = True 
remaining_ids = set(d.keys())


while c != N : 
	c1 = c // Ns 
	c2 = c % Ns 
	pprintt(t)
	if is_going_up :
		g = get_choices(t,c1,c2,remaining_ids,d)
		if len(g) == 0 :
			is_going_up = False
			c -= 1
		else : 
			dict_choices[c] = g
			t[c1][c2] = g[0]
			remaining_ids.remove(g[0][0])
			c += 1
	else :
		g = dict_choices[c]
		a = g.pop(0)
		if a[2] == 3 and a[3] == 1 :
			remaining_ids.add(a[0])
		if len(g) == 0 : 
			remaining_ids.add(t[c1][c2][0])
			t[c1][c2] = None
			c -= 1
		else :
			is_going_up = True 
			dict_choices[c] = g 
			t[c1][c2] = g[0]
			if g[0][0] in remaining_ids:
				remaining_ids.remove(g[0][0])
			c += 1

#way too long because there are very few identical borders
#but it's pretty to look at so I kept it that way		
pprintt(t)
print(t[0][0][0] * t[Ns-1][0][0] * t[0][Ns-1][0] * t[Ns-1][Ns-1][0])

t2 = [[None]*Ns for i in range(Ns)]
for i in range(Ns) :
	for j in range(Ns) :
		tv = t[i][j]
		t2[i][j] = list(map(lambda x : x[1:-1],tr(tv[1],tv[2],tv[3])[1:-1]))

k = len(t2[0][0])
fp = [["." for i in range(Ns*k)] for j in range(Ns*k)]
for i in range(Ns*k) :
	for j in range(Ns*k) :
		fp[i][j] = t2[i//k][j//k][i%k][j%k]
		

fpf = fp 
for r in range(4) :
	for s in range(2) :
		fpf = tr(fp,r,s)
		n = find_sm(fpf)
		if n > 0 :
			m = sum(map(lambda x:x.count("#"),fpf)) - n*15
			print(m)
			break 