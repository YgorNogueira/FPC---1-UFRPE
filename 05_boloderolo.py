# -*- coding: utf-8 -*-

u"""
Bolo de Rolo.

Aluno: Bruno Olimpio dos Santos.
"""


def maximo(lista):
    u"""Tamanho máximo em que se pode dividir as fatias."""
    maximo = lista[0]
    for i in lista:
        if maximo < i:
            maximo = i
    return maximo


def fatias(tamanhos, largura):
    """Em quantas fatias iguais um conjunto pode ser dividido."""
    fatias = 0
    for i in tamanhos:
        fatias = fatias + (i//largura)
    return fatias


N = int(input())
K = int(input())
bolos = input().split(' ')
bolos = [int(i) for i in bolos]

maior = 0

for i in range(1, maximo(bolos)):
    print ('Tamanho: ', i, '---', 'Fatias: ', fatias(bolos, i))
    if fatias(bolos, i) == N:
        maior = i

print(maior)
