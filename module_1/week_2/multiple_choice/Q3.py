def count_word(file_path):
    file = open(file_path, "r")
    text_data = file.read().lower().replace("\n", " ")
    file.close()
    word_arr = text_data.split(" ")
    counter = {}
    for word in word_arr:
        if counter.get(word):
            counter[word] += 1
        else:
            counter[word] = 1
    return counter


file_path = 'module_1\week_2\P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
