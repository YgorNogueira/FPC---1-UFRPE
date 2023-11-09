# Ler entrada
nmr_de_pessoas = int(input())
tempos = []

#Adicionar marcação de tempo baseado no nmr de pessoas
for j in range (nmr_de_pessoas):
    tempos.append(int(input()))

#Contar quantidade de marcações de tempo do sensor
tempo_da_escada = 0
for i in range(nmr_de_pessoas - 1):
   total = tempos[i+1] - tempos[i]
   tempo_da_escada += 10 if total >= 10 else total
tempo_da_escada += 10

#Saída
print(tempo_da_escada)



