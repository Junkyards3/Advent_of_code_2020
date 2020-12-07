f = open("input7.txt","r")
s = f.read()
f.close()

d = dict()
dt = dict()
ts = s.split("\n")

#construire les deux graphes : d est le graphe de la relation "contient"
#et dt le graphe de la relation "est contenu par"
for l in ts :
	lc = l.split("contain")
	key = tuple((lc[0].split(" "))[:2])
	values = lc[1].split(",")
	tk = []
	for v in values : 
		vs = (v.strip()).split(" ")
		if not vs[0].isnumeric() :
			break
		vl = (vs[1],vs[2])
		vv = int(vs[0])
		tk.append([vl,vv])
		if vl in dt :
			dt[vl].append((key,vv))
		else :
			dt[vl] = [(key,vv)]
		if not vl in d :
			d[vl] = []
	if not key in dt :
		dt[key] = []
	d[key] = tk
	
#on met a -1 parce que le shiny gold bag
#ne se contient pas lui meme
nb_sacs = -1
nb_sacs2 = 0
explored = dict()
for k in dt.keys() :
	explored[k] = False 

#parcours en profondeur 
def explore(g,node) :
	global nb_sacs
	explored[node] = True
	nb_sacs += 1
	for (key,vv) in g[node] :
		if not explored[key] :
			explore(g,key)

#pas un vrai parcours de graphe, on passe plusieurs fois
#par un meme noeud en fonction du sac dans lequel on est
#mult prend en compte le nombre de sacs actuel	
def explore2(g,node,mult) :
	global nb_sacs2
	for (key,vv) in g[node] :
		nb_sacs2 += vv*mult
		explore2(g,key,mult*vv)
			
explore(dt,("shiny","gold"))
print(nb_sacs)
explore2(d,("shiny","gold"),1)
print(nb_sacs2)