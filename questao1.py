#ortografia

#a distancia entre duas palavras é o número de operações descritas abaixo q são precisas

#1-Retirar uma letra de A
#2 adicionar uma letra em qualquer poisição de A
#3- trocar uma letra de A por outra na mesma posição

"""RESTRIÇÕES"""
#Uma palavra P pode se referir a uma palavra D do dicionario se estiver
#A uma distancia maxima 2 de D, ou seja, duas operaçoes de distancia
#saída tem q ter uma linha p cada palavra a ser verificada
#cada linha da saída tem que ter todas as palavras do dicionario que a fornecida pode se referir
#se tiver mais de uma palavra, elas tem que ser separadas por um espaço em branco, aparecendo na ordem da entrada




#Dicionario
dicionario_de_palavras = ['pato','pateta', 'caneca']

#Distancia entre duas palavras
def distancia_entre_palavras(palavra1, palavra2):
    if palavra1 == palavra2:
        return 0
    elif len(palavra1) == len(palavra2):
        return 1
    elif len(palavra1) == len(palavra2) + 1:
        return 1
    elif len(palavra1) == len(palavra2) - 1:
        return 1
    elif len(palavra1) == len(palavra2) + 2:
        return 2
    elif len(palavra1) == len(palavra2) - 2:
        return 2
    else:
        return 3


#Entrada
n, m = map(int, input().split())
palavras_do_dicionario = []
for i in range(n):
    palavras_do_dicionario.append(str(input()))

palavras_para_verificar = []
for i in range(m):
    palavras_para_verificar.append(str(input()))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#operações

palavra = palavras_para_verificar[i] #palavra a ser verificada
#posição da letra a ser verificada
for i in range(len(palavra)):
    posicao_da_letra = i

def retirar_letra(palavra, posicao_da_letra):
    return palavra[:posicao_da_letra] + palavra[posicao_da_letra+1:]


def adicionar_letra(palavra, posicao_da_letra, letra):
    return palavra[:posicao_da_letra] + letra + palavra[posicao_da_letra:]


def trocar_letra_por_outra(palavra, posicao_da_letra, letra):
    return palavra[:posicao_da_letra] + letra + palavra[posicao_da_letra+1:]



#Checar se alguma palavra se refere a alguma palavra do dicionario
for palavra in palavras_para_verificar:
    for i in range(len(palavra)):
        for letra in 'abcdefghijklmnopqrstuvwxyz':
            if trocar_letra_por_outra(palavra, i, letra) in palavras_do_dicionario:
                trocar_letra_por_outra(palavra, i, letra)
    for i in range(len(palavra)):
        for letra in 'abcdefghijklmnopqrstuvwxyz':
            if adicionar_letra(palavra, i, letra) in palavras_do_dicionario:
                adicionar_letra(palavra, i, letra)
    for i in range(len(palavra)):
        for letra in 'abcdefghijklmnopqrstuvwxyz':
            if retirar_letra(palavra, i) in palavras_do_dicionario:
                retirar_letra(palavra, i)
            else:
                break


#Saída
for i in range(len(palavras_para_verificar)):
    for palavra in palavras_do_dicionario:
        if distancia_entre_palavras(palavras_para_verificar[i], palavra) <= 2:
            print(palavra, end=' ')
    print() #pula linha


                





        












