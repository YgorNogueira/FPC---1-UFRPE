entrada = int(input())
for caso in range(1, entrada+1):
    n, b = map(int, input().split())
    chamadas = [1, 1] + [0] * (n-1)
    for i in range(2, n+1):
        chamadas[i] = (chamadas[i-1] + chamadas[i-2] + 1) % b
    digito_final = chamadas[n]
    print(f'Case {caso}: {n} {b} {digito_final}')