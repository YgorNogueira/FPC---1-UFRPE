cnt=0
#loop
T = int(input())
for i in range(T):
	cnt += 1
	entr = input()
	e = entr.split()
	a = int(e[0])
	c = int(e[1])
	
	for i in range(c-1):
		b = (a*i) % c
		if b == 1:
			break
	if b == 1:	
		print('Caso %d: %d' %(cnt, i))
	else: 
		print('Caso %d: Muito difícil' %(cnt))
	
	
	
