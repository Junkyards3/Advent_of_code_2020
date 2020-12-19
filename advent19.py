f = open("input19.txt","r")
l = f.read()
f.close()
	
tx = l.split("\n\n")
rules = dict()
for a in tx[0].split("\n") :
	r = a.split(": ")[1]
	if r[0] == "\"" :
		rules[int(a.split(":")[0])] = ("c",r[1])
	else :
		rules[int(a.split(":")[0])] = ("s",list(map(lambda x:list(map(int,x.split())),r.split("|"))))

di = dict()
dl = dict()

for i in rules :
	t,v = rules[i]
	if i not in dl :
		dl[i] = set([])
	if t == "s":
		for j in [n for sublist in v for n in sublist] :
			if j not in di :
				di[j] = set([])		
			dl[i].add(j)
			di[j].add(i)


s = set([0])
dag = []

while len(s) > 0 :
	v = s.pop()
	dag.append(v)
	for w in dl[v] :
		di[w].remove(v)
		if len(di[w]) == 0 :
			s.add(w)

acc_m = dict()
dag.reverse()

def make_mess(l_mess) :
	if len(l_mess) == 1 :
		return l_mess[0] 
	else :
		l2 = make_mess(l_mess[1:])
		return [x + b for x in l_mess[0] for b in l2]

for i in dag :
	tr,vr = rules[i]
	if tr == "c" :
		acc_m[i] = [vr]
	else :
		acc_m[i] = []
		for sr in vr :
			n = []
			for jr in sr :
				n.append(acc_m[jr])
			acc_m[i] += make_mess(n)
		
s = 0
for l in tx[1].split("\n") :
	if l in acc_m[0] :
		s += 1
print(s)

l42 = len(acc_m[42][0])
l31 = len(acc_m[31][0])
def validn(m) :
	global acc_m,l31,l42
	if m in acc_m[0] :
		return True 
	else :
		n42 = 0
		n31 = 0
		while m[:l42] in acc_m[42] :
			n42 += 1
			m = m[l42:]

		while m[-l31:] in acc_m[31] :
			n31 += 1
			m = m[:-l31]

		return n42 > n31 and n31 >= 1 and m == "" 


s2 = 0
for l in tx[1].split("\n") :
	if validn(l) :
		s2 += 1
print(s2)
