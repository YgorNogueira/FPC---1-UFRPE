#FILA

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def is_empty(self):
        return self.inicio == None or self.fim == None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.ant = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no

    def remover(self):
        if self.is_vazia():
            return None
        no_removido = self.inicio
        prox = self.inicio.proximo
        prox.ant = None
        self.inicio = prox
        return no_removido
        
    def __str__(self):
        i = self.inicio
        s = ''
        while i is not None:
            s += f"{i} |"
            i = i.proximo
            return s
entrada = list(range(1, 11))
fila= fila()
for i in entrada:
    fila.inserir(i)
print(fila)
