'''
Vou mandar comentado pq sou gente boa
Quiser outros códigos comentados ou tirar dúvidas só me chamar
email: italusousa@gmail.com

'''

class Aviao():
	
	#estrutura da classe que foi pedido na questão
	def __init__(self, consumo, cidade, combustivel=0.00):
		self.consumo = consumo
		self.cidade_atual = cidade
		self.nivel_tanque = combustivel
	
	#adicionando combustível no avião
	def abastecer(self, qtdLitros):
		self.nivel_tanque += qtdLitros
	
	#retorna os valores atuais do objeto
	def status(self):
		print("local:%s, tanque: %.2f" %(self.cidade_atual, self.nivel_tanque))
		
	#método que faz o avião mudar de lugar e consumir combustível
	def voar(self, origem, destino, distancia):
		consumo_viagem = distancia/self.consumo #fazer isso antes pra poder verificar(ver1) se o que tem de combustível da pra fazer a viagem
		if origem == self.cidade_atual: #você precisa saber se a cidade de origem está certa ou errada
			if self.nivel_tanque >= consumo_viagem: # ver1
				self.nivel_tanque -= consumo_viagem
				self.cidade_atual = destino
			else: 
				print("combustivel insuficiente")
		else: 
			print("origem invalida")

#Aqui abre o plano de voo
arq = open("planovoo.txt", "r", encoding="utf-8")
planoDeVoo = arq.readlines()
arq.close()

#aqui estaremos ajustando nossas entradas
comandos = []
for linha in planoDeVoo:
	j = linha.replace('\n', '')#vai usar isso em basicamente todos os programas que precisar ler arquivos, inclusive no projeto
	k = j.replace(',', '.')#só por causa de uma entrada estranha que ele colocou, ele colocou o valor flutuante assim: 3,0 e pro python ler tem que ser 3.0 (com ponto)!
	comandos.append(k)# coloco numa nova lista os arquivos ajustados, já que não pode modificar a lista atual pois está num laço
	
#na questão as 2 primeiras linhas são para a construção do objeto, logo eu retiro eles da lista de comandos que serão usados depois
consumo = float(comandos.pop(0))
cidadeAtual = comandos.pop(0)# o da posição 0 denovo pois quando eu retiro o anterior essa entrada fica na posição 0 da lista atualizada
aviao = Aviao(consumo, cidadeAtual)#crio o objeto

for entrada in comandos:
	comando = entrada.split(":")# para poder ler os comandos com vários métodos
	if comando[0] == "abastecer" or comando[0] == "combustivel":
			aviao.abastecer(float(comando[1]))
	if comando[0] == "status":
		aviao.status()
	if len(comando) == 3: # o detalhe é aqui, a unica forma que encontrei para poder ler sem da erro, se você fizer lendo como da outra forma da um erro. 
		aviao.voar(comando[0], comando[1], int(comando[2]))
	if comando[0] == "fim":
		break
