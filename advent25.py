import math

def mod_exp(base, exp, mod) :
	if exp == 0 : 
		return 1
	if exp % 2 == 0:
		r = mod_exp(base, exp // 2, mod)
		return (r * r) % mod
	else: 
		r = mod_exp(base, exp // 2, mod)
		return (r * r * base) % mod
		
card_key = 3248366
door_key = 4738476

t = [1]
c = 0
found_card = False
found_door = False
door_lps = 0

#baby step giant step to find the loop size 
bsgs = dict()
m = int(math.sqrt(20201226)+1)
alpha = 7
alphaj = 1
for j in range(m) :
	bsgs[alphaj] = j 
	alphaj = (alphaj * alpha) % 20201227
gamma = door_key
alphamm = mod_exp(alphaj,20201225,20201227)
for i in range(m) :
	if gamma in bsgs :
		door_lps = i*m + bsgs[gamma]
		break 
	else :
		gamma = (gamma * alphamm) % 20201227

#fast exponential to end
print(mod_exp(card_key,door_lps,20201227))