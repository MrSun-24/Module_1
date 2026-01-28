def my_function(n):
    min_value = n[0]
    for i in range(1, len(n)):
        if n[i] < min_value:
            min_value = n[i]
    return min_value

my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))