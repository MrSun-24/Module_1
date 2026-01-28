def count_char(s):
    char_dict = {}

    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

print(count_char('smiles'))