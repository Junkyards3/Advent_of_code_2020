def next(t) :
	pos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	tr = []
	n = len(t)
	for i in range(n) :
		tr.append([])
		m = len(t[i])
		for j in range(m) :
			nb_occ_seats = 0
			for (x,y) in pos :
				if i+x >= 0 and i+x < n and j+y >= 0 and j+y < m :
					nb_occ_seats += 1 if t[i+x][j+y] == "#" else 0
			if t[i][j] == "L" and nb_occ_seats == 0:
				tr[i].append("#")
			elif t[i][j] == "#" and nb_occ_seats >= 4 :
				tr[i].append("L")
			else :
				tr[i].append(t[i][j])
	return tr

def next2(t) :
	pos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	tr = []
	n = len(t)
	for i in range(n) :
		tr.append([])
		m = len(t[i])
		for j in range(m) :
			nb_occ_seats = 0
			for (x0,y0) in pos :
				x = x0
				y = y0
				while i+x >= 0 and i+x < n and j+y >= 0 and j+y < m :
					if t[i+x][j+y] == "." :
						x += x0 
						y += y0 
					else :
						nb_occ_seats += 1 if t[i+x][j+y] == "#" else 0
						break
			if t[i][j] == "L" and nb_occ_seats == 0:
				tr[i].append("#")
			elif t[i][j] == "#" and nb_occ_seats >= 5 :
				tr[i].append("L")
			else :
				tr[i].append(t[i][j])
	return tr
	
def pret_print(t):
	r = ""
	for l in t :
		r += "".join(l) + "\n"
	return r
t = []

import time
st = time.time()
f = open("input11.txt","r")
for l in f :
	t.append(list(l.replace("\n","")))
f.close()

tf = t 
tf2 = next(t)

while tf != tf2 : 
	tf_temp = tf2
	tf2 = next(tf2)
	tf = tf_temp

print(pret_print(tf2).count("#"))

tf = t 
tf2 = next2(t)

while tf != tf2 : 
	tf_temp = tf2
	tf2 = next2(tf2)
	tf = tf_temp

print(pret_print(tf2).count("#"))
print(time.time()-st)
#this takes so much time