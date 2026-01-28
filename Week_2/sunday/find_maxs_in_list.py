def solution1(num_list, k):
    first_slicing_window = num_list[:k]
    result = [max(first_slicing_window)]

    for i in range(k, len(num_list)):
        first_slicing_window.append(num_list[i])
        if len(first_slicing_window) >= k:
            del first_slicing_window[0]
            result.append(max(first_slicing_window))
    #     print(first_slicing_window)
    # print(result)
    return result

def solution2(num_list, k):
    list_tmp = list()
    result = []
    for i in num_list:
        list_tmp.append(i)
        if len(list_tmp) == k:
            result.append(max(list_tmp))
            del list_tmp[0]
    return result

def solution3(num_list, k):
    start_indexs = list(range(0, len(num_list) - k + 1))
    end_indexs = list(range(k, len(num_list) + 1))
    result = []
    for start_index, end_index in zip(start_indexs, end_indexs):
        sub_list = num_list[start_index: end_index]
        result.append(max(sub_list))
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(solution1(num_list, k))
print(solution2(num_list, k))
print(solution3(num_list, k))