def olympics(olympics):
    # Lê a entrada do usuário.
    n, m = map(int, input().split())
    medals = [[0, 0, 0] for _ in range(n)]
    for _ in range(m):
        gold, silver, bronze = map(int, input().split())
        medals[gold - 1][0] += 1
        medals[silver - 1][1] += 1
        medals[bronze - 1][2] += 1

    # Cria uma lista para guardar os países e suas pontuações.
    countries = []
    for i in range(n):
        countries.append((medals[i][0], medals[i][1], medals[i][2], i + 1))

    # Ordena a lista de países pelas pontuações.
    for i in range(len(countries) - 1):
        for j in range(i + 1, len(countries)):
            if countries[i][0] < countries[j][0]:
                countries[i], countries[j] = countries[j], countries[i]
            elif countries[i][0] == countries[j][0] and countries[i][1] < countries[j][1]:
                countries[i], countries[j] = countries[j], countries[i]
            elif countries[i][0] == countries[j][0] and countries[i][1] == countries[j][1] and countries[i][2] < countries[j][2]:
                countries[i], countries[j] = countries[j], countries[i]

    # Imprime os países.
    for country in countries:
        print(country[3], end=" ")

olympics(olympics)

#Não usei heap por não entender muito bem a lógica, estou tendo certa dificuldade na disciplina.
#Logo, tentei fazer com a ajuda do copilot.