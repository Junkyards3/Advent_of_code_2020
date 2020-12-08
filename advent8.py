l_ins = []

f = open("input8.txt","r")

for l in f :
	l_ins.append((l[0],int(l[4:])))
	
f.close()

n = len(l_ins)

def run(l_ins):
	pos = 0
	visited = []
	acc = 0
	while pos >= 0 and pos < n :
		if pos in visited :
			return (True,acc)
		else :
			visited.append(pos)
			i,v = l_ins[pos]
			if i == "j" :
				pos += v 
			elif i == "a" :
				acc += v
				pos += 1
			else :
				pos += 1
	return (False,acc)

print(run(l_ins)[1])
for i in range(n) :
	if l_ins[i][0] == "a" :
		continue 
	elif l_ins[i][0] == "j":
		l_ins[i] = ("n",l_ins[i][1])
		b,a = run(l_ins)
		if not b :
			break
		l_ins[i] = ("j",l_ins[i][1])
	else :
		l_ins[i] = ("j",l_ins[i][1])
		b,a = run(l_ins)
		if not b :
			break
		l_ins[i] = ("n",l_ins[i][1])
print(a)