t = []
f = open("input2.txt","r")
for l in f :
	tl = l.split(" ")
	to_add = []
	to_add.append(list(map(int,tl[0].split("-"))))
	to_add.append(tl[1][0])
	to_add.append(tl[2].replace("\n",""))
	t.append(to_add)
f.close()
nb_valid = 0
for [nbs,c,s] in t :
	n = s.count(c)
	if n >= nbs[0] and n <= nbs[1] :
		nb_valid += 1
print(nb_valid)

nb_valid = 0
for [nbs,c,s] in t :
	if bool(s[nbs[0]-1] == c) != bool(s[nbs[1]-1] == c) :
		nb_valid += 1
print(nb_valid)