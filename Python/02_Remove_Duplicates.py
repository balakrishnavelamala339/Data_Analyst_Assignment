text = input("Enter string: ")
result = ""

for char in text:
    if char not in result:
        result += char

print("Unique string:", result)