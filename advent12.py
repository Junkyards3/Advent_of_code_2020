import numpy as np

f = open("input12.txt","r")
t = []
for l in f :
	t.append((l[0],int(l[1:].replace("\n",""))))
f.close()

dt = dict()
dt["N"] = np.array([0,1])
dt["S"] = np.array([0,-1])
dt["W"] = np.array([-1,0])
dt["E"] = np.array([1,0])

da = dict()
da[0] = "E"
da[90] = "S"
da[180] = "W"
da[270] = "N"

p = np.array([0,0])
angle = 0
for (c,n) in t :
	if c == "F":
		p += dt[da[angle]]*n
	elif c == "L" :
		angle = (angle - n)%360
	elif c == "R" :
		angle = (angle+n)%360
	else :
		p += dt[c]*n
		
print(sum(map(abs,p)))

da2 = dict()
da2[90] = np.array([[0,-1],[1,0]])
da2[180] = np.array([[-1,0],[0,-1]])
da2[270] = np.array([[0,1],[-1,0]])
p = np.array([0,0])
pwr = np.array([10,1])
for (c,n) in t :
	if c == "F":
		p = p+pwr*n
	elif c == "L" :
		pwr = np.matmul(da2[n],pwr)
	elif c == "R" :
		pwr = np.matmul(da2[-n%360],pwr)
	else :
		pwr = pwr + dt[c]*n
print(sum(map(abs,p)))