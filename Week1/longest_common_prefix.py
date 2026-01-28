# def longestCommonPrefix(strs):
#     first_element = strs[0]    #flower
#     count = 0
#     for i in range(1, len(strs)): #flow -> 1, flight -> 2
#         for j in range(len(first_element)): #len(flower) = 6 <-> 1 -> 5
#             if j >= len(strs[i]): 
#                 break
#             else:
#                 if first_element[j] == strs[i][j]:
#                     print(first_element, first_element[j], strs[i][j])
#                     count += 1
#                 else:
#                     first_element = first_element[0: count]
#                     count = 0
#     return first_element[0: count]
            
strs = ['flower', 'flow', 'flight']
# longestCommonPrefix(strs)
# first_element = strs[0]
# for i in range(1, len(strs)):
#     count = 0
#     print(f'vong lap {i}, {count}')
#     for j in range(len(first_element)):
#         if j >= len(strs[i]) or first_element[j] != strs[i][j]:
#             break
#         count += 1
#         print(f'vong lap {i} - {j}, {count}')
#         print(first_element[j], strs[i][j])
#     first_element = first_element[0: count]
#     print(first_element)

def longestCommonPrefix(strs):
    first_str = strs[0]
    for s in strs[1:]:
        while (not s.startswith(first_str)):
            first_str = first_str[:-1]
        print(first_str)
    return first_str

print(longestCommonPrefix(strs))