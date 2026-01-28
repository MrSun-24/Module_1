file_name = "P1_data.txt"
def open_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

data = open_file(file_name)
# print(data)

def data_processing(data):
    data = data.replace('\n', ' ')
    data = data.lower()
    data = data.split()
    return data

words = data_processing(data)

def word_counting(words):
    counter = {}

    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

print(word_counting(words))