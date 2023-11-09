L, C, M, N = map(int, input().split())
terrain = []
for _ in range(L):
    lines = list(map(int, input().split()))
    terrain.append(lines)

lines = len(terrain)
columns = len(terrain[0])   
result = 0

group = [[0] * (columns + 1) for x in range(lines + 1)]
for i in range(1, lines + 1):
    for j in range(1, columns + 1):
        group[i][j] = group[i-1][j] + group[i][j-1] - group[i-1][j-1] + terrain[i-1][j-1]

for i in range(M, lines + 1):
    for j in range(N, columns + 1):
        submatrizes = group[i][j] - group[i-M][j] - group[i][j-N] + group[i-M][j-N]
        result = submatrizes if submatrizes > result else result

print(result)
