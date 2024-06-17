# Testing variables
test_num_list = [3, 1, -2, -1, 5, 4]
test_k = 2

# Define function
def get_max_sliding_window(num_list, k):
    sliding_window = []
    res = []
    for element in num_list:
        sliding_window.append(element)
        if len(sliding_window) == k:
            res.append(max(sliding_window))
            del sliding_window[0]
    print(res)

# Call function
get_max_sliding_window(test_num_list, test_k)
