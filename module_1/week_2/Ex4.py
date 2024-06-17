# Testing variables
test_source = 'apple'
test_target = 'appee'


# Define function
def edit_distance(source, target):
    distances = []

    # create matrix
    for i in range(len(source) + 1):
        row = [0]*(len(target) + 1)
        distances.append(row)

    # update value for row index 0 and column index 0
    for i in range(len(source) + 1):
        distances[i][0] = i
    for i in range(len(distances[0])):
        distances[0][i] = i

    del_cost = 0
    ins_cost = 0
    sub_cost = 0

    # update value for others index
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                del_cost = distances[i - 1][j]
                ins_cost = distances[i][j - 1]
                sub_cost = distances[i - 1][j - 1]

                distances[i][j] = min(del_cost, ins_cost, sub_cost) + 1

    print(distances[-1][-1])


# Call function
edit_distance(test_source, test_target)
