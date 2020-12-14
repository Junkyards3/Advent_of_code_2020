def comp_m_and_plus(m) :
	if len(m) == 0 :
		return (0,0)
	else :
		mm = comp_m_and_plus(m[:-1])
		mm_and,mm_plus = 2*mm[0],2*mm[1]
		mm_and += 0 if m[-1] == "X" else 1
		mm_plus += 1 if m[-1] == "1" else 0
		return (mm_and,mm_plus)

def comp_all_floatings(m) :
	if len(m) == 0 : 
		return [""]
	else : 
		mm = comp_all_floatings(m[:-1])
		if m[-1] == "X" :
			mm2 = []
			for v in mm :
				mm2.append(v + "0")
				mm2.append(v + "1")
			return mm2
		else :
			mm2 = []
			for v in mm :
				mm2.append(v + "0")
			return mm2
			
def or_str(s1,s2) :
	s = ""
	for i in range(len(s1)) :
		if s1[i] == "0" and s2[i] == "0" :
			s += "0"
		else : 
			s += "1"
	return s 
	
def and_str(s1,s2) :
	s = ""
	for i in range(len(s1)) :
		if s1[i] == "1" and s2[i] == "1" :
			s += "1"
		else : 
			s += "0"
	return s 

def construct(add,mask,fl) :
	s = ""
	for i in range(len(add)) :
		if mask[i] == "X" :
			s = s + fl[i]
		else :
			s = s + add[i]
	return s
	
f = open("input14.txt","r")
l = f.read()
f.close()
	
t = l.split("\nmask")
t = list(map(lambda x:x.split("\n"),t))
mem = dict()
for e in t :
	m = e[0].split(" = ")[1]
	m_and,m_plus = comp_m_and_plus(m)
	for i in range(1,len(e)) :
		si = e[i].split(" = ")
		vi = int(si[1])
		mi = int(si[0][4:-1])
		tvi = vi - (vi & m_and) + m_plus 
		mem[mi] = tvi 
		
print(sum(mem.values()))
	
mem = dict()
for e in t :
	m = e[0].split(" = ")[1]
	all_floatings = comp_all_floatings(m)
	for i in range(1,len(e)) :
		si = e[i].split(" = ")
		vi = int(si[1])
		mi = str(bin(int(si[0][4:-1])))[2:]
		mi = "0"*(36-len(mi)) + mi
		mi2 = or_str(mi,m.replace("X","0"))
		for fl in all_floatings :
			add = construct(mi2,m,fl)
			mem[add] = vi 

print(sum(mem.values()))