f = open("input16.txt","r")
l = f.read()
f.close()
	
t = list(map(lambda x:x.split("\n"),l.split("\n\n")))
l_cond = []
l_field = []
for l in t[0] :
	l_cond_i = []
	li = l.split(": ")[1]
	lv = li.split(" or ")
	for c in lv :
		lvv = c.split("-")
		l_cond_i.append((int(lvv[0]),int(lvv[1])))
	l_cond.append((l.split(": ")[0],l_cond_i[:]))

l_nby_t = list(map(lambda x:x.split(","),t[2][1:]))
err_rate = 0
valid_tickets = []

for tk in l_nby_t :
	tkn = list(map(int,tk))
	is_valid_ticket = True
	for v in tkn : 
		is_valid = False
		for field,cond in l_cond :
			for rang in cond :
				if v >= rang[0] and v <= rang[1] :
					is_valid = True
					break
			if is_valid :
				break
		if not is_valid :
			err_rate += v
			is_valid_ticket = False
	if is_valid_ticket :
		valid_tickets.append(tkn)
			
print(err_rate)

field_pos = dict()
for field,cond in l_cond : 
	v = list(range(len(l_cond)))
	field_pos[field] = v
	
for tkn in valid_tickets :
	for i in range(len(tkn)):
		v = tkn[i]
		for field,cond in l_cond :
			is_valid_field = False
			for rang in cond :
				if v >= rang[0] and v <= rang[1] :
					is_valid_field = True
					break
			if not is_valid_field : 
				field_pos[field].remove(i)
				
field_final = dict()
while field_pos : 
	for field in field_pos.keys() :
		if len(field_pos[field]) == 1 :
			v = field_pos[field][0]
			field_final[field] = v
			field_pos.pop(field)
			for field2 in field_pos.keys() :
				field_pos[field2].remove(v)
			break
			
my_tk = list(map(int,t[1][1].split(",")))
r = 1
for k in field_final : 
	if k.split(" ")[0] == "departure" :
		r *= my_tk[field_final[k]]
		
print(r)