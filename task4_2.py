import re

def convert (camel_input):
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+', camel_input)
    return '_'.join(map(str.lower, words))
test_strings = ["FirstItem", "FriendsList", "MyTuple"]
for test_string in test_strings:
    print(convert(test_string))
