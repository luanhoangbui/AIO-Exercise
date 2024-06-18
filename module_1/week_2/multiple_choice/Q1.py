def max_kernel(num_list, k):
    sliding_window = []
    res = []
    for element in num_list:
        sliding_window.append(element)
        if len(sliding_window) == k:
            res.append(max(sliding_window))
            del sliding_window[0]
    return res


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
