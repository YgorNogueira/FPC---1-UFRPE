#Lavando louça
class No:

  def init(self,data=None):  #python aceita parâmetro default --> dado=None
    #NÃO BOTA NADA MUTÁVEL, SOMENTE IMUTÁVEIS NO PARÂMETRO DEFAULT
    #self é um ponteiro para si mesmo, aquele objeto
    self.data = data
    self.next = None
    self.bef = None

  def str(self):
    return f"Dado: {self.data}"


class Fila:

  def init(self):
    self.start = None
    self.end = None

  def is_empty(self):
    return self.start is None or self.end is None

  def put(self, data):
    #first thing to do is to alocate memory
    new_no = No(data)
    if self.is_empty():
      self.start = new_no
      self.end = new_no
    else:
      new_no.bef = self.end
      self.end.next = new_no
      self.end = new_no

  def remove(self):
    if self.is_empty():
      return None
    else:
      self.end = None
    #if self.start == self.end:
    no_removed = self.start
    proximo = self.start.next
    #self.start.next.bef = None
    if proximo is not None:
      proximo.bef = None
    self.start = next
    return no_removed.data

  def str(self):
    i = self.start
    s = ""
    while i is not None:
      s += f"{i} |"
      i = i.next
    return s

  def inserir_em_lote(self, lista):
    for i in lista:
      self.put(i)


#entrada
n_festas = int(input())
for festa in range(n_festas):
  mesa = [int(i) for i in input().split()]
  jogadores = []
  while mesa[0] != -1:
    cartas_jogador = [int(i) for i in input().split()]
    fila_cartas = Fila()
    fila_cartas.inserir_em_lote(cartas_jogador)
    jogadores.append(fila_cartas)
#jogo
  cont_rodadas = 0
  carta_mesa_idx = 0
  ganhou = False
  while not ganhou and cont_rodadas < 1000:
    carta_vez = mesa[carta_mesa_idx]
    #Comparações das cartas
    for idx, jogador in enumerate(jogadores):
      carta_jogador = jogador.remove()
      if carta_jogador is None:
        print(idx + 1)
        ganhou = True
        break
      if carta_vez != carta_jogador:
        jogador.put(carta_jogador)
    #circular as cartas da mesa
    carta_mesa_idx = (carta_mesa_idx + 1) % len(mesa)
    cont_rodadas += 1
  if not ganhou:
    print(0)