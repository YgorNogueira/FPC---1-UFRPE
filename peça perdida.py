"""Peça perdida - Ygor Fellipe Macêdo Nogueira"""
nmr_pecas = int(input())
lista_de_entrada = [int(i) for i in input().split()]
for n in range(1, nmr_pecas + 1):
    achou = False
    for l in lista_de_entrada:
        if n == l:
            achou = True
            break

    if not achou:
        print(n)
        break


"# A linha 1 solicita ao usuário a entrada de um número inteiro que representa a quantidade total de peças no \
quebra cabeça"

"# Enquanto a linha 2 solicita a entrada de números separados, que serão recebidos como um string representando a lista\
de peças desejadas e logo após, convertidos em números inteiros"

"# Em seguida, teremos um loop, onde a variável booleana Achou estará inserida, sendo essa variável responsável por \
determinar se o número ``n´´ é encontrado na lista de entrada"

"# Após isso, teremos outro loop que itera por cada elemento da lista de entrada.\
Dentro desse loop será verificado se ``n´´ está dentro da lista n == l, se for verdadeiro, achou será definida como\
e o script sairá do loop interno usando ``break´´"

"# Por conseguinte, fora do loop, verificamos se ``achou´´ é False. Se for verdadeiro, o script irá printar ``n´´ e\
sairá do loop externo usando outro ``break´´"

"# Logo, o script irá imprimir o primeiro número ausente na lista de entrada e irá ser encerrado."