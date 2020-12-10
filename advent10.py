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

nb_arr = 1
ls = sorted(list(nb_occur.keys()))
nb_perms = [1,1,2]
for i in range(1,ls[-1]+1) :
	if i > len(nb_perms) :
		nb_perms.append(nb_perms[-1]+nb_perms[-2]+nb_perms[-3])
	nb_arr *= nb_perms[i-1]**nb_occur[i]
print(nb_arr)