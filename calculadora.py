def suc(n):
    n=n+1
    return n
def soma(a, b):
    for i in range(b):
        a = suc(a)
    return a

def mult(a, b):
    result = 0
    for i in range(b):
        result = soma(result, a)
    return result

def exp(a, b):
    result = 1
    for i in range(b):
        result = mult(result, a)
    return result

"""# Da linha 1 até aqui temos as definições das funções da calculadora usando a lógica de sucessão \
como por exemplo na função de soma, onde ela itera b vezes adicionando 1 número a ``a´´ em cada repetição."""


"""# Nas linhas 27 e 28, dois comandos para poder separar as operações em somente \
uma entrada, por isso desenvolvi esse raciocínio"""

resultado = []

while True:
    entrada = input().split()
    if len(entrada) >= 2:
        operacao = entrada[0]
        a = int(entrada[1])

    if len(entrada) >= 3:
        b = int(entrada[2])

    if operacao == "Suc":
        resultado.append(suc(a))
    if operacao == "Soma":
        resultado.append(soma(a, b))
    if operacao == "Mult" or operacao == "Multi":
        resultado.append(mult(a, b))
    if operacao == "Exp":
        resultado.append(exp(a, b))
    if not entrada:
        break

print("Resultados:")
Resultados=len(resultado)
for j in range(Resultados-1):
    print(resultado[j])
