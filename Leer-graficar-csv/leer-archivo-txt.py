""" # my_file = open("C:/Users/DELL/OneDrive/Escritorio/DUDAS PYTHON.txt")
my_file = open(
    "C:/Users/DELL/OneDrive/Escritorio/Nuevo documento de texto.txt")

# print(my_file.read())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close() """

with open(
        "C:/Users/DELL/OneDrive/Escritorio/Nuevo documento de texto.txt") as my_file:
    for line in my_file:
        print(line)
