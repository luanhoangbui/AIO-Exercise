def my_function(x):
    # your code here
    reverse_x = ''
    for i in range(len(x) - 1, -1, -1):
        reverse_x += x[i]
    return reverse_x


x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))
