t = []
f = open("input5.txt","r")
s = set()
for l in f :
	l = l.replace("\n","")
	vr = int("".join(list(map(lambda x: "1" if x == "B" else "0",l[:7]))),2)
	vc = int("".join(list(map(lambda x: "1" if x == "R" else "0",l[7:]))),2)
	id = 8*vr + vc 
	s.add(id)
f.close()
print(max(s))
sp = set(range(min(s),max(s)+1))
print(sp.difference(s))
