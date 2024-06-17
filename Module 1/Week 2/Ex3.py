# Testing variables
test_file_path = 'Module 1\Week 2\P1_data.txt'


# Define function
def count_word(file_path):
    # read and reprocessing text file
    file = open(file_path, "r")
    text_data = file.read().lower().replace("\n", " ")
    file.close()

    # split into words_array
    word_arr = text_data.split(" ")
    res = {}
    for word in word_arr:
        if res.get(word):
            res[word] += 1
        else:
            res[word] = 1
    print(res)


# Call function
count_word(test_file_path)
