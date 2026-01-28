def check_the_nunber(N):
    list_of_numbers = []
    for i in range(1, 5):
        list_of_numbers.append(i)
    result = True if N in list_of_numbers else False
    return result

N = 7
assert check_the_nunber(N) == False
N = 2
results = check_the_nunber(N)
print(results)