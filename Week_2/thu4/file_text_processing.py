file_name = "data.txt"
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read() #dữ liệu đã được copy vào bộ nhớ ram (trong biến data)
    return data.split(',')
print(read_data(file_name))
data = read_data(file_name)

def fill_missing_with_average(data):
    missing_value = [i for i, x in enumerate(data) if len(x) == 0] 
    non_missing_value = [float(x) for x in data if len(x) > 0]
    # print(missing_value)
    # print(non_missing_value)
    average = sum(non_missing_value) / len(non_missing_value)
    for index in missing_value:
        data[index] = average
    return data
print(fill_missing_with_average(data))
print(data)

def write_data(file_name):
    with open(file_name, 'w') as file:
        file.write(','.join(str(x) for x in data))

write_data(file_name)
print(read_data(file_name))