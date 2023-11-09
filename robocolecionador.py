#Professor, me perdoe mas dessa vez não irei comentar, fiz esse código de 1 da manhã.
#Obrigado pela atenção e desculpe o transtorno.
#Espero que esse código esteja certo.
#Atenciosamente, Ygor.
while True:
    N, M, S = map(int, input().split())
    if N == 0 and M == 0 and S == 0:
        break
    matrix = [['#' for _ in range(M+2)] for _ in range(N+2)]
    x = y = 0
    direction = ""
    for i in range(N):
        line = input()
        for j in range(M):
            matrix[i+1][j+1] = line[j]
            if line[j] == 'N':
                direction = 'N'
                y, x = i+1, j+1
            elif line[j] == 'S':
                direction = 'S'
                y, x = i+1, j+1
            elif line[j] == 'L':
                direction = 'L'
                y, x = i+1, j+1
            elif line[j] == 'O':
                direction = 'O'
                y, x = i+1, j+1
    colect = 0

    inst = input()
    if 'F' not in inst:
        print(0)
    else:
        for i in range(len(inst)):
            if inst[i] == 'E':
                if direction == 'N':
                    direction = 'O'
                elif direction == 'O':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'L'
                else:
                    direction = 'N'
            elif inst[i] == 'D':
                if direction == 'N':
                    direction = 'L'
                elif direction == 'L':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'O'
                else:
                    direction = 'N'
            else:
                x_or, y_or = x, y
                if direction == 'N':
                    y -= 1
                elif direction == 'S':
                    y += 1
                elif direction == 'O':
                    x -= 1
                elif direction == 'L':
                    x += 1
                if matrix[y][x] == "#":
                    x, y = x_or, y_or
                if matrix[y][x] == '*':
                    colect += 1
                    matrix[y][x] = '.'
        print(colect)