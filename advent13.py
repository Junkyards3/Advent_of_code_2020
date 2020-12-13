from operator import mul
from functools import reduce 

f = open("input13.txt","r")
l = f.read()
f.close()

t = l.split("\n")
first_id = int(t[0])
current_id = first_id
buses_id = list(map(int,list(filter(lambda x : x.isnumeric(),t[1].split(",")))))
correct_bus_id = 0
found_correct = False
while not found_correct :
	for bus_id in buses_id : 
		if current_id % bus_id == 0 :
			correct_bus_id = bus_id 
			found_correct = True 
			break 
	if not found_correct : 
		current_id += 1

print(correct_bus_id*(current_id - first_id))

def xgcd(a,b) :
	pu,u = 1,0
	pv,v = 0,1
	while b != 0 :
		q, r = divmod(a,b)
		u,pu = pu-q*u,u
		v,pv = pv-q*v,v 
		a,b = b,r 
	return a,pu,pv
	
def inv_mod(a,p) :
	return xgcd(a,p)[1]

def crt(l_p,l_v):
	if len(l_v) == 1 :
		return l_v[0]
	else :
		c = crt(l_p[1:],l_v[1:])
		lb = reduce(mul,l_p[1:],1)
		m = inv_mod(lb,l_p[0])*(l_v[0]-c)
		return (c + lb*m) % (lb*l_p[0])
	
l_p = []
l_v = []
tv = t[1].split(",")
for i in range(len(tv)) :
	if tv[i] != "x" :
		l_p.append(int(tv[i]))
		l_v.append(-i)
		
print(crt(l_p,l_v))


			
			
