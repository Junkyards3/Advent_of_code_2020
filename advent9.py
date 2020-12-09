t = []

f = open("input9.txt","r")
for l in f :
	t.append(int(l))
f.close()

n = len(t)
v = 0
for k in range(25,n) :
	v = t[k]
	i = k-25
	found = False
	while i < k and not found :
		j = i+1
		while j < k and not found :
			if t[i]+t[j] == v and t[i] != t[j] :
				found = True
			j += 1
		i += 1
	if not found :
		print((k,v))
		break
		
for l in range(2,n) :
	s = sum(t[0:l])
	sp = 0
	while s != v and sp + l < n :
		sp += 1
		s += (t[sp+l-1] - t[sp-1])
	if s == v :
		print(min(t[sp:sp+l])+max(t[sp:sp+l]))
		break