n_colunas = int(input())
colunas = [int(x) for x in input().split()]

soma = 0
for i in colunas:
    soma += i

n_pedras_escada = int(n_colunas * (n_colunas + 1) / 2)
if (soma - n_pedras_escada) % n_colunas != 0:
    print(-1)
else:
    base = int((soma  - n_pedras_escada) / n_colunas)
    n_movimentos = 0
    for idx, coluna in enumerate(colunas):
        if coluna > base + idx + 1:
            n_movimentos += coluna - (base + idx + 1)
    print(n_movimentos)
