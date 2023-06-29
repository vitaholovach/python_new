with open('text.txt', 'r') as file:
    text = file.read()
result = set()

for letters in text.lower():
    if letters.isalpha():
        result.update({f'{letters} - {text.count(letters)}'})
for letters in result:
    print(letters)
