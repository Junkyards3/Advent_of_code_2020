f = open("input15.txt","r")
l = f.read()
f.close()
	
t = list(map(int,l.replace("\n","").split(",")))
last_seen = dict()
k = len(t)
pn = t[-1]

for i in range(k) :
	last_seen[t[i]] = i 

for i in range(k-1,29999999) :
	if pn in last_seen :
		nn = i - last_seen[pn]
	else :
		nn = 0
	last_seen[pn] = i
	t.append(nn)
	pn = nn
	
print(t[2019])
print(t[29999999])