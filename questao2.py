#Tomando de volta

#Levar o maior número possível de itens sem exceder a capacidade da mochila
#Cada item tem um peso e um valor definidos por 
# N = número de itens
# C = capacidade da mochila
# As outras linhas vao conter os pesos e os valores
# O peso nao pode exceder C

#Entrada
N, C = map(int, input().split())
pesos_e_valores = []

for i in range(N):
    peso, valor = [int(i) for i in input().split()]
    pesos_e_valores.append((peso, valor))

#Ordenar os itens para levar o maior valor possível
def ordenar_itens(pesos_e_valores):
    for i in range(len(pesos_e_valores)):
        for j in range(len(pesos_e_valores) - i - 1):
            if pesos_e_valores[j][1] < pesos_e_valores[j + 1][1]:
                pesos_e_valores[j], pesos_e_valores[j + 1] = pesos_e_valores[j + 1], pesos_e_valores[j]
    return pesos_e_valores

#Escolher itens para levar baseado no menor peso e no maior valor
def escolher_itens(pesos_e_valores, C):
    itens_escolhidos = []
    peso_total = 0
    for i in range(len(pesos_e_valores)):
        if peso_total + pesos_e_valores[i][0] <= C:
            itens_escolhidos.append(pesos_e_valores[i])
            peso_total += pesos_e_valores[i][0]
    return itens_escolhidos

#Calcular o valor total dos itens escolhidos
def valor_total(itens_escolhidos):
    valor_total = 0
    for i in range(len(itens_escolhidos)):
        valor_total += itens_escolhidos[i][1]
    return valor_total

print(valor_total(escolher_itens(ordenar_itens(pesos_e_valores), C)))




