Binary_code = input("Input Binary: ")

x = Binary_code.split()

decoded = ""

for char in x:
    text = int(char, 2)
    letter = chr(text)
    decoded += letter
print(letter)
print(decoded)