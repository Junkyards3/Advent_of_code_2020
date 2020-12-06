f = open("input6.txt","r")
s = f.read()
f.close()

ts = s.split("\n\n")
print(sum(map(lambda x:len(set(x.replace("\n",""))),ts)))
print(sum(map(lambda x:len(set.intersection(*list(map(set,x.split("\n"))))),ts)))