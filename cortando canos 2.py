user_input = [int(x) for x in input().split()]
a_list = []
b_list = []


for i in range(user_input[0]):
    pipes = [int(x) for x in input().split()]
    for i in range(user_input[1] // pipes[0]):
      a_list.append(pipes[0])
      b_list.append(pipes[1])


items_nmbr = len(a_list)
limit = user_input[1]


T = [[0 for j in range (limit + 1)] for i in range(items_nmbr + 1)]
for j in range(1, limit+1):
    for i in range(1, items_nmbr+1):
        if a_list[i - 1] > j:
            T[i][j] = T[i - 1][j]
        else:
            T[i][j] = max(T[i - 1][j], T[i - 1][j - a_list[i - 1]]+b_list[i-1])


print(T[items_nmbr][limit])