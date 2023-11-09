def dist_edit(a ,b):
    #a = 'pata'
    #b = 'pato'

    tab = []

    num = 0
    num2 = 0
    tab.append([i for i in range(len(b)+1)])

    for i in range(1, len(a)+1):
        tab.append([])
        for j in range(len(b)+1):
            if j == 0:
                tab[i].append(i)
            else:
                #tab[i].append(0)
                if a[i-1] == b[j-1]:
                    tab[i].append( tab[i-1][j-1])
                else:
                    tab[i].append( min(tab[i][j-1], tab[i-1][j-1], tab[i-1][j])+1 )        
    return tab[len(a)][len(b)]

dic = []
lista = []

NM = input().split()
for i in range(int(NM[0])):
	dic.append(input())
	
for i in range(int(NM[1])):
	lista.append(input())

for inpt in lista:
    saida = []
    for p_dic in dic:
        if len(p_dic) >= len(inpt)-2 and len(p_dic) <= len(inpt)+2:
            if len(p_dic) >= len(inpt)-2 and len(p_dic) <= len(inpt)+2:
                edit_dist = dist_edit(inpt, p_dic)
                if edit_dist <= 2:
                    saida.append(p_dic)

    palavra = ' '
    print(palavra.join(saida))	