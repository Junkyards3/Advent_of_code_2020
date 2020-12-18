def to_npi(s) :
	t = s.replace(" ","")
	output = []
	qop = []
	for c in s :
		if c.isnumeric() :
			output.append(int(c))
		elif c == "(" :
			qop.append(c)
		elif c == "+" or c == "*" :
			while len(qop) != 0 and (qop[-1] == "+" or qop[-1] == "*") :
				output.append(qop[-1])
				qop = qop[:-1]
			qop.append(c)
		elif c == ")":
			while qop[-1] != "(" :
				output.append(qop[-1])
				qop = qop[:-1]
			qop = qop[:-1]
	while len(qop) != 0 :
		output.append(qop[-1])
		qop = qop[:-1]
	return output

def comp(s) :
	t = to_npi(s)
	stack = []
	for c in t :
		if c == "+" :
			stack[-2] += stack[-1]
			stack = stack[:-1]
		elif c == "*" :
			stack[-2] *= stack[-1]
			stack = stack[:-1]
		else :
			stack.append(c)
	return stack[0]

def to_npi2(s) :
	t = s.replace(" ","")
	output = []
	qop = []
	for c in s :
		if c.isnumeric() :
			output.append(int(c))
		elif c == "(" :
			qop.append(c)
		elif c == "*" :
			while len(qop) != 0 and (qop[-1] == "+" or qop[-1] == "*") :
				output.append(qop[-1])
				qop = qop[:-1]
			qop.append(c)
		elif c == "+" :
			while len(qop) != 0 and qop[-1] == "+" :
				output.append(qop[-1])
				qop = qop[:-1]
			qop.append(c)
		elif c == ")":
			while qop[-1] != "(" :
				output.append(qop[-1])
				qop = qop[:-1]
			qop = qop[:-1]
	while len(qop) != 0 :
		output.append(qop[-1])
		qop = qop[:-1]
	return output
	
def comp2(s) :
	t = to_npi2(s)
	stack = []
	for c in t :
		if c == "+" :
			stack[-2] += stack[-1]
			stack = stack[:-1]
		elif c == "*" :
			stack[-2] *= stack[-1]
			stack = stack[:-1]
		else :
			stack.append(c)
	return stack[0]
	
f = open("input18.txt","r")
l = f.read()
f.close()
	
t = l.split("\n")
s = 0
s2 = 0
for l in t :
	s += comp(l)
	s2 += comp2(l)
print(s)
print(s2)