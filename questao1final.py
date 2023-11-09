"""Para desencorajar pássaros como corvos e pardais de se alimentarem de suas
colheitas, Roberval precisava colocar alguns espantalhos em seu campo de milho.
Seu sobrinho Juvenal realmente gosta de robôs, e sugeriu que ele usasse um
espantalho de robôs: "Um único espantalho robô pode proteger melhor todo o
campo de milho e vai durar muito mais do que dez campos tradicionais!", Ele
disse. Como Roberval acha que seu sobrinho é um garoto esperto, ele seguiu seu
conselho e comprou um robô espantalho. O robô se move ao longo de um
caminho que circunda o campo de milho. No caminho, existem estações de
carregamento automáticas, numeradas sequencialmente no sentido horário a
partir de 1. A figura abaixo mostra um campo com oito estações de carregamento"""

"""O robô começa todos os dias na estação número 1 e recebe uma sequência de
comandos que devem ser realizados em ordem durante o dia. Esses comandos
são gerados com base em algoritmos de aprendizado de máquina com dados
coletados por sensores espalhados pelo campo de milho, garantindo uma
cobertura ideal da colheita. Cada comando faz com que o robô se mude para
outra estação de carregamento próximo àquela em que está atualmente, no
sentido horário ou anti-horário.
Apesar das promessas de cobertura ideal feitas por Juvenal, no final de um
determinado dia o agricultor encontrou parte de sua colheita devastada. Para
descobrir o que pode ter acontecido, Roberval quer saber quantas vezes o robô
esteve na estação de carregamento mais próxima à área devastada. Dado o
número da estação mais próxima à área devastada e a sequência de comandos
para um único dia, você poderia ajudar o fazendeiro a encontrar esse número?"""

"""Entrada
A primeira linha contém três números inteiros N, C e S, representando
respectivamente o número de estações de carregamento ( 2<=N<=100 ), o
número de comandos (1<=C<=1000 ) e a estação de carregamento mais próxima
à área devastada (1<=S<=N). A segunda linha contém C inteiros X1; X2; ...; XC ,
representando a sequência de comandos recebidos pelo espantalho robô. Para i =
1; 2; ...; C, se Xi for 1, então o i-ésimo comando significa “mover para a próxima
estação de carregamento no sentido horário”, enquanto que se Xi for -1, o i-
ésimo comando significa “mover para a próxima estação de carregamento no
sentido anti-horário”. O robô sempre começa na estação número 1."""

"""Saída
Produza uma única linha com um número inteiro indicando o número de vezes
que o robô esteve na estação S durante o dia."""

#entrada
n, c, s = map(int, input().split())
comandos = list(map(int, input().split()))
estacao_atual = 1
cont = 0
if s == 1:
    cont = 1

def proxima_estacao(estacao_atual, comandos):
    for i in range (len(comandos)):
        if comandos[i] == 1:
            estacao_atual += 1

def voltar_estacao(estacao_atual, comandos):
    for i in range (len(comandos)):
        if comandos[i] == -1:
            estacao_atual -= 1

def verificar_estacao(estacao_atual, s):
    if estacao_atual == s:
        cont += 1
        
#processamento e saída
for i in range (len(comandos)):
    proxima_estacao(estacao_atual, comandos)
    verificar_estacao(estacao_atual, s)
    voltar_estacao(estacao_atual, comandos)
    verificar_estacao(estacao_atual, s)
print(cont)




