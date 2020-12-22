f = open("input22.txt","r")
l = f.read()
f.close()
	
t = list(map(lambda x:x.split(":")[1][1:].split("\n"),l.split("\n\n")))
d1 = list(map(int,t[0]))
d2 = list(map(int,t[1]))

while len(d1) > 0 and len(d2) > 0 :
	c1 = d1.pop(0)
	c2 = d2.pop(0)
	if c1 > c2 :
		d1 += [c1,c2]
	else :
		d2 += [c2,c1]

print(sum(map(lambda i : (d1+d2)[i]*(len(d1+d2)-i),range(len(d1+d2)))))
d1 = list(map(int,t[0]))
d2 = list(map(int,t[1]))

def rec_com_d1w(d1,d2,game) :
	conf = []
	round = 1
	while not (d1,d2) in conf and len(d1) > 0 and len(d2) > 0:
		conf += [(d1.copy(),d2.copy())]
		round += 1
		c1 = d1.pop(0)
		c2 = d2.pop(0)
		if len(d1) < c1 or len(d2) < c2 :
			if c1 > c2 :
				d1 += [c1,c2]
			else :
				d2 += [c2,c1]
		else :
			d1w,dck1 = rec_com_d1w(d1[:c1].copy(),d2[:c2].copy(),game+1)
			if d1w :
				d1 += [c1,c2]
			else :
				d2 += [c2,c1]
	if (d1,d2) in conf :
		return True,d1
	else:
		return len(d2)==0,d1+d2
	
print(sum(map(lambda i : (rec_com_d1w(d1,d2,1)[1])[i]*(len(d1+d2)-i),range(len(d1+d2)))))