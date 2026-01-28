def my_function(integers, number = 1):
    results = []
    for i in integers:
        check = True if i == number else False
        results.append(check)
    return results

my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == [False, False, False, False]

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))