'''
por: Ítalo Sousa
'''

#vars
sala = []
cadeirasCompradas = []
view = []
idDaCompra = []
caixa = 0
ingressosDevolvidos = 0
ingressosVendidos = 0

while True:
	try:
		#Tamanho da sala
		nLinhas = int(input("Informe o número de linhas: "))
		nColunas = int(input("Informe o número de colunas: "))
		break
	except ValueError:
		print("Erro! Insira um numero inteiro.")

#zfill
nZfill = len(str((nLinhas*nColunas)-1))

#criar matriz
for i in range(nLinhas):
	sala.append([0]*nColunas)

#adicionando as cadeiras na sala
acumulador = 0
for i in range(nLinhas):
	for j in range(nColunas):
		sala[i][j] = str(acumulador).zfill(nZfill)
		acumulador += 1

#criar matriz view
for i in range(nLinhas):
	view.append([0]*nColunas)

#adicionando as cadeiras na view
acumulador = 0
for i in range(nLinhas):
	for j in range(nColunas):
		view[i][j] = str(acumulador).zfill(nZfill)
		acumulador += 1
		
#interface - sala de cinema
print("")
for i in sala:
	print("| " + " ".join(i) + " |")

#interface - opções
print("\nBem vindo ao sistema de venda de ingressos.")
while True:
	print("\nEscolha a operação:")
	print("1- Comprar ingressos")
	print("2- Devolver ingressos")
	print("3- Resumo das vendas")
	print("4- Sair")
	opc = input("\nDigite sua escolha: ")
	
	if opc == "4":
		#relatório
		print("\n|------- Relatório --------|")
		print("|Quantidade de ingressos vendidos: %i" %ingressosDevolvidos)
		print("|Quantidade de ingressos devolvidos: %i" %ingressosDevolvidos)
		print("|Valor total apurado: R$%i"",00" %caixa)
		print("|----------------------------|")
		break
	
	elif opc == "1":
		#compra de ingressos
		print("Compra de ingressos --------")
		
		#interface - sala de cinema
		print("")
		for i in view:
			print("| " + " ".join(i) + " |")
		print("")
		
		#comprando
		while True:
			#vars
			opcCompra = []
			cadeiraX = []
			cadeiraY = []
			coordenada = []
			ok = 0
			cadeiraComprada = 0
			intOpc = -1
			#entrada
			opc = input("Assento(s) que deseja comprar: ")
			if opc == "c":
				print("\nOperação cancelada")
				break
			elif ok == 1:
				break
			else:
				#ajuste das entradas
				opc = opc.split(",")
				if opc != "":
					for i in opc:
						if i != "":
							opcCompra.append(i.zfill(nZfill))
					#para cada cadeira
				else:
					break
				for cadeira in opcCompra:
					try:
						intOpc = int(cadeira)
					except ValueError:
						print("")
					if intOpc >= 0:
						if (intOpc > (nColunas*nLinhas)-1):
							break
						else: #coordenada X da cadeira
							x = 0 
							x = intOpc//nColunas
							cadeiraX.append(x)
						
							#coordenada y	da cadeira
							iD = str(intOpc).zfill(nZfill)
							cadeiraY.append(sala[x].index(iD))
					else:
						cadeiraComprada += 1
				#fim do for
				
				#CHECKOUT
				#verificando se tem compradas
				for cadeira in opcCompra:
					if cadeirasCompradas.count(cadeira) != 0:
						cadeiraComprada += 1
					if opcCompra.count(cadeira) > 1:
						cadeiraComprada += 1
				
				#Liberação de compra
				if (cadeiraComprada == 0) and (intOpc <= (nColunas*nLinhas)-1):
					totalCompra = 0
					print("\n|--------- Checkout ---------|")
					print("|cadeira ----------- preço --|")
					#finalização da compradas
					
					#adicionando nas compradas
					for cadeira in opcCompra:
						cadeirasCompradas.append(cadeira)
						print("|%s ---------------- R$10,00 |" %cadeira)
						totalCompra += 10
						
					#substituindo na view	
					k = 0
					for i in cadeiraX:
						j = cadeiraY[k]
						view[i][j] = "X"*nZfill
						k += 1
					print("|---------- TOTAL -----------|")
					print("| R$%i"",00"%totalCompra)
					print("|----------------------------|")
					caixa += totalCompra
					break
				#Escolha outras cadeiras
				else:
					print("Indisponível, Escolha outra(s) cadeira(s)!")
		
		#fim do while
	#fim opc 1
	elif opc == "2":
		#devolução de ingressos
		print("Devolução de ingressos --------")
		
		#interface - sala de cinema
		print("")
		for i in view:
			print("| " + " ".join(i) + " |")
		print("")
		
		#devolvendo
		while True:
			#vars
			opcDevolucao = []
			cadeiraX = []
			cadeiraY = []
			ok = 0
			cadeiraComprada = 0
			#entrada
			opc = input("Assento(s) que deseja Devolver: ")
			if opc == "c":
				print("\nOperação cancelada")
				break
			elif ok == 1:
				break
			else:
				#ajuste das entradas
				opc = opc.split(",")
				for i in opc:
					opcDevolucao.append(i.zfill(nZfill))
				#para cada cadeira
				for cadeira in opcDevolucao:
					try:
						intOpc = int(cadeira)
					except ValueError:
						print("")
					if intOpc >= 0:
						if (intOpc > (nColunas*nLinhas)-1):
							break
						else: #coordenada X da cadeira
							x = 0 
							x = intOpc//nColunas
							cadeiraX.append(x)
						
							#coordenada y	da cadeira
							iD = str(intOpc).zfill(nZfill)
							cadeiraY.append(sala[x].index(iD))
				#fim do for
				
				#CHECKOUT
				#verificando se tem
				n = 0
				cadeiraNexiste = 0
				cadeiraComprada = 0
				for cadeira in opcDevolucao:
					if cadeirasCompradas.count(cadeira) == 0:
						cadeiraNexiste += 1
					if opcDevolucao.count(cadeira) >= 2:
						cadeiraComprada += 1
				
				#Liberação de devolucao
				if (cadeiraComprada == 0) and (intOpc <= (nColunas*nLinhas)-1) and (cadeiraNexiste == 0):
					totalCompra = 0
					print("\n|-------- Devolucao ---------|")
					print("|cadeira ------------ preço -|")
					#finalização da devolvidas
					
					#tirando das compradas
					for cadeira in opcDevolucao:
						endereco = cadeirasCompradas.index(cadeira)
						cadeirasCompradas.pop(endereco)
						print("|%s ----------------- R$9,00 |" %cadeira)
						totalCompra += 9
						ingressosDevolvidos += 1
						
					#substituindo na view	
					k = 0
					for i in cadeiraX:
						j = cadeiraY[k]
						view[i][j] = sala[i][j]
						k += 1
					print("|---------- TOTAL -----------|")
					print("| R$%i"",00"%totalCompra)
					print("|----------------------------|")
					print("|Só devolvemos 90% do valor do ingresso")
					print("|----------------------------|")
					caixa -= totalCompra
					break
				#Escolha outras cadeiras
				else:
					print("Indisponível, Escolha outra(s) cadeira(s)!")
					cadeiraComprada = 0
		
		#fim do while
		
	elif opc == "3":
		#resumo das vendas
		print("\nResumo das vendas --------")
		print("\n|----------------------------|")
		print("|Ocupação da sala no momento: %i" %len(cadeirasCompradas))
		print("|Quantidade de ingressos devolvidos: %i" %ingressosDevolvidos)
		print("|Valor total apurado: R$%i"",00" %caixa)
		print("|----------------------------|")
	
	else:
		print("Opção inválida, tente novamente!")
