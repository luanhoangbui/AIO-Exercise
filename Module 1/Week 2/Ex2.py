# Testing variables
test_str = 'Happiness'


# Define function
def count_character(str):
    res = {}
    for char in str:
        number_of_char = res.get(char)
        if number_of_char:
            res[char] += 1
        else:
            res.setdefault(char, 1)
    print(res)


# Call function
count_character(test_str)
