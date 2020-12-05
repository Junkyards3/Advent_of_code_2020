f = open("input4.txt","r")
nb_valid = 0
buffer = ""
valid_set = {'pid', 'ecl', 'byr', 'eyr', 'hcl', 'iyr', 'hgt'}
for l in f :
	if l[0] == "\n" :
		bkv = buffer.split()
		s = set(map(lambda x:x.split(":",1)[0],bkv))
		if valid_set <= s :
			nb_valid += 1
		buffer = ""
	else :
		buffer += l
f.close()
print(nb_valid)

f = open("input4.txt","r")
nb_valid = 0
buffer = ""
valid_set = {'pid', 'ecl', 'byr', 'eyr', 'hcl', 'iyr', 'hgt'}
valid_letters = {'a','b','c','d','e','f'}
valid_eye = {"amb","blu","brn","gry","grn","hzl","oth"}
for l in f :
	if l[0] == "\n" :
		bkv = buffer.split()
		d = dict()
		for x in bkv :
			xt = x.split(":",1)
			d[xt[0]] = xt[1]
		#print(d)
		if valid_set <= set(d.keys()) :
			if d["byr"].isnumeric() and int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002 :
				if d["iyr"].isnumeric() and int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020 :
					if d["eyr"].isnumeric() and int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030 :
						unit_hgt = d["hgt"][-2:]
						v_hgt = d["hgt"][:-2]
						if v_hgt.isnumeric() and ((unit_hgt == "cm" and int(v_hgt) >= 150 and int(v_hgt) <= 193) or 
						(unit_hgt == "in" and int(v_hgt) >= 59 and int(v_hgt) <= 76)) :
							if d["hcl"][0] == '#' and (len(d["hcl"]) == 7 and
							all(map(lambda x: x in valid_letters or x.isnumeric(),d["hcl"][1:]))) :
								if d["ecl"] in valid_eye :
									if len(d["pid"]) == 9 and d["pid"].isnumeric() :
										nb_valid += 1
										#print("ok\n")
		buffer = ""
	else :
		buffer += l
f.close()
print(nb_valid)
