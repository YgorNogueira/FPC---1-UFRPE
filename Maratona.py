#usa raw_input por causa de erro no run.codes
a = raw_input()
b = raw_input()

li1 = a.split()
li2 = b.split()

dist_inter = int(li1[1])

#print(dist_inter, li1,li2)

posto = [int(i) for i in li2]
n_consegue = 0

for i in range(len(li2)-1):
	#print(i, i+1)
	if posto[i+1] - posto[i] > dist_inter:
		n_consegue += 1

if n_consegue >= 1:	
	print('N')
else:
	print('S')