def character_count(word):
    character_statistic = {}
    for char in word:
        number_of_char = character_statistic.get(char)
        if number_of_char:
            character_statistic[char] += 1
        else:
            character_statistic.setdefault(char, 1)
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
