#numeros de teste

n = int(input())

#loop dos testes

for i in range(1, n+1):
    n, k = [int (i) for i in input().strip().split(' ')]

    vivo = 0
    for j in range(1, n+1):
        vivo = (vivo + k) % j

    print("Case {}: {}".format(i, vivo+1))
