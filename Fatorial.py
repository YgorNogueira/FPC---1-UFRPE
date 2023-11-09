def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

n = int(input())
num = n
r = 1  
soma = 0
k = 0

while True:
	if fact(r) > num:
		soma += fact(r-1)
		num -= fact(r-1)
		r = 1
		k += 1
	else:
		r += 1
	if soma == n:
		break
print	(k)