def levenshtein_distance(token1, token2):
    distances = []

    # create matrix
    for i in range(len(token1) + 1):
        row = [0]*(len(token2) + 1)
        distances.append(row)

    # update value for row index 0 and column index 0
    for i in range(len(token1) + 1):
        distances[i][0] = i
    for i in range(len(distances[0])):
        distances[0][i] = i

    del_cost = 0
    ins_cost = 0
    sub_cost = 0

    # update value for others index
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                del_cost = distances[i - 1][j]
                ins_cost = distances[i][j - 1]
                sub_cost = distances[i - 1][j - 1]

                distances[i][j] = min(del_cost, ins_cost, sub_cost) + 1

    return float(distances[-1][-1])


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))
