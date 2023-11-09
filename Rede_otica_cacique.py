def procura(arvores, v):
    indice_v = None
    cnt = 0
    for arvore in arvores:
        if v in arvore:
            indice_v = cnt
        cnt += 1
    return indice_v

def kruskal(m, n, arestas, vertices):
    resultante = {}
    ar = [ set(i) for i in vertices ]
    #print(ar)
    e = sorted(arestas, key=arestas.get)
    for i in e:
        #print(i)
        a = procura(ar, i[0])
        b = procura(ar, i[1])
        if a != b:
            cnjb = ar.pop(procura(ar, i[0]))
            cnja = ar.pop(procura(ar, i[1]))
            ar.append(cnja.union(cnjb))
            resultante[ (i[0], i[1]) ] = arestas[(i[0], i[1])]

    return resultante

# arestas = {
#     ('1', '2'): 10,
#     ('2', '3'): 5,
#     ('3', '1'): 7
# }

def start(m , n, arestas, vertices):
    arvores = {}
    
    resultante = kruskal(m, n, arestas, vertices)

    f = [ sorted(i) for i in resultante ]
    for i in sorted(f):
        saida = ''
        for j in i:
            saida += str(j) + ' '
        print(saida[:-1])

def main():
    cnt = 1
    while 1:
        e1 = input().split()
        n, m = int(e1[0]), int(e1[1])        
        if n is 0:
            break
        else:
            if cnt != 1:
                print(' ')
            print('Teste %d' %cnt)
            arestas = {}
            vertices = set()
            for i in range(m):
                e2 = input().split()
                a, b, p = e2[0], e2[1], int(e2[2])
                arestas[(a, b)] = p
                vertices.update(a, b)
            start(m, n, arestas, vertices)
            
            #print(arestas)
            #print(vertices)

            
        cnt += 1
            
        

main()