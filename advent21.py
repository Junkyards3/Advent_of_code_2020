f = open("input21.txt","r")
l = f.read()
f.close()
	
poss_ingr = dict()
poss_allg = dict()
final_ingr = dict()
all_ingrs = []

t = l.split("\n")
for e in t :
	ev = e[:-1].replace(",","").split(" (contains ")
	ingrs = ev[0].split(" ")
	allgs = ev[1].split(" ")
	all_ingrs += ingrs
	for allg in allgs :
		if allg in poss_ingr :
			poss_ingr[allg] = poss_ingr[allg].intersection(set(ingrs))
		else :
			poss_ingr[allg] = set(ingrs)
			
can_clean = True

while can_clean :
	can_clean = False
	for allg in poss_ingr :
		if len(poss_ingr[allg]) == 1 :
			can_clean = True
			ingr = poss_ingr[allg].pop()
			final_ingr[allg] = ingr
			for allg2 in poss_ingr : 
				if ingr in poss_ingr[allg2] :
					poss_ingr[allg2].remove(ingr)
			poss_ingr.pop(allg)
			break


no_allgs = set(all_ingrs).difference(set(final_ingr.values()))
print(sum(map(lambda x:all_ingrs.count(x),no_allgs)))

allgs_alpha = sorted(final_ingr.keys())
print(",".join(list(map(lambda x :final_ingr[x],allgs_alpha))))