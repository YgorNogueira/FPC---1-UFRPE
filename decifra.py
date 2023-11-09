sequencia = input()
frase = input()
alfabeto = "abcdefghijklmnopqrstuvwxyz"
descriptografado = ''
for letra in frase:
    descriptografado = descriptografado + (alfabeto[sequencia.index(letra)])

print(descriptografado)



"""m = len(palavras_para_verificar)
n = len(palavras_do_dicionario)
for palavra in palavras_para_verificar:
    for palavra_do_dicionario in palavras_do_dicionario:
        if distancia_entre_palavras(palavra, palavra_do_dicionario) <= 2:
            print(palavra_do_dicionario, end=' ')
    print() #pula linha"""

"""for palavra in palavras_para_verificar:
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
                retirar_letra(palavra, i)"""