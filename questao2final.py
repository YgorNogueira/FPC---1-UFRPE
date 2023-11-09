#Juvenal vai ao Banco brigar

#Declara a classe nó
class No(): 
    def __init__(self, valor, ponteiro=None):
        self.__valor = valor
        self.__ponteiro = ponteiro

    def __str__(self):
        return str(self.__valor)

    def get_value(self):
        return self.__valor

    def set_value(self, valor):
        self.__valor = valor

    def get_ponteiro(self):
        return self.__ponteiro

    def set_ponteiro(self, valor):
        self.__ponteiro = valor

class Lista():
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def __str__(self):
        if self.lista_ta_vazia():
            return '0'
        no_atual = self.__inicio
        string = ''
        while no_atual is not None:
            if no_atual.get_ponteiro() is None:
                string += str(no_atual.get_value())
            else:
                string += str(no_atual.get_value()) + ' '
            no_atual = no_atual.get_ponteiro()
        return string

    def lista_ta_vazia(self):
        return self.__inicio is None

    def adicionar_no_fim(self, valor):
        novo_no = No(valor)
        if self.lista_ta_vazia():
            self.__inicio = self.__fim = novo_no
        else:
            self.__fim.set_ponteiro(novo_no)
            self.__fim = novo_no

    def adicionar_no_inicio(self, valor):
        novo_no = No(valor)
        if self.lista_ta_vazia():
            self.__inicio = self.__fim = novo_no
        else:
            novo_no.set_ponteiro(self.__inicio)
            self.__inicio = novo_no

    def tira_do_inicio(self):
        if self.lista_ta_vazia():
            return 'Vc n pode remover uma Lista vazia seu animal'
        valor_primeiro_no = self.__inicio.get_value()
        if self.__inicio is self.__fim:
            self.__inicio = self.__fim = None
        else:
            self.__inicio = self.__inicio.get_ponteiro()
        return valor_primeiro_no

    def tira_do_fim(self):
        if self.lista_ta_vazia():
            return 'Vc n pode remover uma Lista vazia seu animal'
        valor_ultimo_no = self.__fim.get_value()
        if self.__inicio is self.__fim:
            self.__inicio = self.__fim = None
        else:
            no_atual = self.__inicio
            while no_atual is not self.__fim:
                no_atual = no_atual.get_ponteiro()
            no_atual.set_ponteiro(None)
            self.__fim = no_atual
        return valor_ultimo_no

    def get_inicio(self):
        return self.__inicio

    def get_fim(self):
        return self.__fim

    def set_inicio(self, valor):
        self.__inicio = valor

    def set_fim(self, valor):
        self.__fim = valor

class Fila(Lista):

    def colocar_na_fila(self, valor):
        self.adicionar_no_fim(valor)

    def tirar_da_fila(self):
        return self.tira_do_inicio()

def funcionamento():
    t = int(input())
    for caso in range(1, t+1):
        n = int(input())
        fila_normal = Fila() 
        fila_preferencial = Fila() 
        print('Caso %i:' %(caso))
        for comandos in range(1, n+1):
            entrada = input().split()
            if entrada[0] == 'I':
                saida = ''
                if fila_normal.lista_ta_vazia():
                    saida += '0'
                else:
                    saida += str(fila_normal.get_inicio())
                saida += ' '
                if fila_preferencial.lista_ta_vazia():
                    saida += '0'
                else:
                    saida += str(fila_preferencial.get_inicio())
                print(saida)
            elif entrada[0] == 'f':
                fila_normal.colocar_na_fila(entrada[1])
            elif entrada[0] == 'p':
                fila_preferencial.colocar_na_fila(entrada[1])
            elif entrada[0] == 'A':
                if fila_normal.lista_ta_vazia():
                    fila_preferencial.tirar_da_fila()
                else:
                    fila_normal.tirar_da_fila()
            elif entrada[0] == 'B':
                if fila_preferencial.lista_ta_vazia():
                    fila_normal.tirar_da_fila()
                else:
                    fila_preferencial.tirar_da_fila()
funcionamento()
