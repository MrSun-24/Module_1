file_name = "data.txt"

def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

data = read_data(file_name)
# print(data)

def data_processing(data):
    data = data.replace(',', '')
    data = data.replace('.', '')
    data = data.replace('-', ' ')
    data = data.replace('  ', ' ')
    data = data.lower()
    return data.split(' ')

data_update = set(data_processing(data))
print(data_update)
data = {value: key for key, value in enumerate(data_update)}
print(data)

def text_classification():
    input_text = input("Enter text: ")
    data_input = data_processing(input_text)
    numerical_data = []

    for i in data_input:
        if i in data:
            numerical_data.append(data[i])
        else:
            numerical_data.append(0)
    print(numerical_data)

text_classification()