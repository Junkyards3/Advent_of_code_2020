t = []
f = open("input1.txt","r")
for l in f :
	t.append(int(l))
f.close()
t.sort()
n = len(t)
c = 0
found = False
while c < n and not found : 
	v = 2020-t[c]
	cc = c + 1
	while cc < n and not found and t[cc] <= v :
		if t[cc] == v :
			found = True
			print("First part")
			print([t[c],t[cc]])
			print(t[c]*t[cc])
			print("\n")
		cc += 1
	c += 1
	
c = 0
found = False
while c < n and not found :
	v = 2020 - t[c]
	cc = c + 1
	while cc < n and not found and t[cc] <= v :
		vv = v - t[cc]
		ccc = c + 1
		while ccc < n and not found and t[ccc] <= v :
			if t[ccc] == vv :
				found = True
				print("Second part")
				print([t[c],t[cc],t[ccc]])
				print(t[c]*t[cc]*t[ccc])
				print("\n")
			ccc += 1
		cc += 1
	c += 1