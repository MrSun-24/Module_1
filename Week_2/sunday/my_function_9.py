def my_function(n):
    max_value = n[0]
    for i in range(1, len(n)):
        if n[i] > max_value:
            max_value = n[i]
    return max_value

my_list = [1, 22, 93, -100]
assert my_function(my_list) == 93

my_list = [1, 2, 3, -1]
print(my_function(my_list))