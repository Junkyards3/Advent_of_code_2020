t = []

f = open("input10.txt","r")
for l in f :
	t.append(int(l))
f.close()

t.sort()
t.append(t[-1]+3)
t.insert(0,0)
n1 = 0
n3 = 0
nb_occur = dict()
curr = 1
for i in range(len(t)-1) :
	v = t[i+1]-t[i]
	if v == 1 :
		n1 += 1
		curr += 1
	elif v == 3 :
		n3 += 1
		nb_occur[curr] = nb_occur.setdefault(curr,0) + 1
		curr = 1
print(n1*n3)

tv = [1]
for x in range(1,len(t)) :
	p = x-1
	v = t[x]
	r = 0
	while p >= 0 and t[p] >= v-3 :
		r += tv[p]
		p -= 1
	tv.append(r)
print(tv[-1])