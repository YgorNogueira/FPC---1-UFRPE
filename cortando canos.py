entrada = [int(x) for x in input().split()]
p = []
v = []

for i in range(entrada[0]):
    canos = [int(x) for x in input().split()]
    p.append(canos[0])
    v.append(canos[1])

n_itens = len(p)
capacidade = entrada[1]

T = [[0 for j in range (capacidade + 1)] for i in range(n_itens + 1)]
for j in range(1, capacidade+1):
    for i in range(1, n_itens+1):
        if p[i - 1] > j:
            T[i][j] = T[i - 1][j]
        else:
            T[i][j] = max(T[i - 1][j], T[i - 1][j - p[i - 1]]+v[i-1])
print(T[n_itens][capacidade])