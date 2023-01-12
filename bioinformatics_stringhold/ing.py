import itertools

all = [-2,-1,1,2]

aa = []
for i in itertools.combinations(all,2):
    i = " ".join(map(str,i))
    i = i.split(" ")
    if int(i[0]) != -int(i[1]):
        aa.append(i)

    
print(aa)


for i in aa:
    print(i)
    print(i[0]); print(i[1])
