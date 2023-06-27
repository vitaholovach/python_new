text = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
string = text.strip().replace("=", "&").replace("&&", "&")
values = string.split("&")
values.remove('sssss')
dict = {}

for element in range(0, len(values), 2):
    key = values[element]
    value = values[element + 1]
    dict[key] = value
print(dict)
