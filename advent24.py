import numpy as np

f = open("input24.txt","r")
l = f.read()
f.close()

t = []
for s in l.split("\n") :
	tt = []
	c = 0
	while c < len(s) :
		k = 1
		if s[c] == "n" or s[c] == "s" :
			k += 1
		tt.append(s[c:c+k])
		c = c+k
	t.append(tt)
	
b = {"ne" : np.array([0,1]),"e" : np.array([1,0]),"se" : np.array([1,-1]),"sw" : np.array([0,-1]),
"w" : np.array([-1,0]),"nw" : np.array([-1,1])}

tiles = set([])
for path in t :
	pos = tuple(sum(map(lambda x:b[x],path)))
	if not pos in tiles :
		tiles.add(pos)
	else :
		tiles.remove(pos)
	
print(len(tiles))
	
def next_step(tiles) :
	neighb = dict()
	newt = set([])
	for tile in tiles :
		for dir in b.values() :
			tilen = tuple(np.asarray(tile)+dir)
			neighb[tilen] = neighb.setdefault(tilen,0) + 1 
	for k in neighb :
		v = neighb[k]
		if k in tiles :
			if v == 1 or v == 2:
				newt.add(k)
		else :
			if v == 2 :
				newt.add(k)
	return newt
				
for k in range(100) :
	tiles = next_step(tiles)

print(len(tiles))