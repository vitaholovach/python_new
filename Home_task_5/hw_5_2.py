import pickle

with open('./test/data directory/data_tuples.txt', 'r+b') as file:
    text = file.read()
list_tuples = pickle.loads(text)
result = []
for element in list_tuples:
    if element[2] == 1:
        result.append(element[0] + element[1])
    elif element[2] == 2:
        result.append(element[0] - element[1])
    else:
        result.append(element[0] * element[1])
print(result)
