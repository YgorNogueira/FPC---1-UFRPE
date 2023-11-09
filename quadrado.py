def soma_da_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

nmr_linhas = int(input())
quadrado = [[0] * nmr_linhas for i in range(nmr_linhas)]

for i in range(nmr_linhas):
  valor = input()
  valor = valor.split()
  for j in range(nmr_linhas):
    quadrado[i][j] = int(valor[j])

somou = soma_da_lista(quadrado[0])
linha_errada = coluna_errada = 0

for i in range(nmr_linhas):
  soma_linhas = soma_da_lista(quadrado[i])
  soma_colunas = soma_da_lista(quadrado[j][i] for j in range(nmr_linhas))
  if soma_linhas != somou:
    linha_errada = i

  if soma_colunas != somou:
    coluna_errada = i

valor_inicial = quadrado[linha_errada][coluna_errada]
valor_final =  somou - (soma_da_lista(quadrado[linha_errada]) - valor_inicial)

print(valor_final, valor_inicial)