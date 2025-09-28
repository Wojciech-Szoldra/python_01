# Otwracie pliku, odczytanie i wyświetlenie całej zawartości, zamknięcie pliku
file_1 = open('D:\\IT\\Programowanie\\testy\\folder do zadan z os\\pliki\\temp\\tyrion_lanister\\quotes.txt',mode='r',encoding='utf-8')

content_1 = file_1.read()
print(f'Cała zawartość pliku: {content_1}')
file_1.close()

# Tutaj robimy to samo za pomocą instrukcji with, która automatycznie zamyka plik.
with open('D:\\IT\\Programowanie\\testy\\folder do zadan z os\\pliki\\temp\\tyrion_lanister\\quotes.txt',mode='r',encoding='utf-8') as file:
    
    content = file.read()
    print(f'Instrukcja with. Cała zawartość pliku : {content}')

# Każda linia pliku będzie osobną pozycją w liście
with open('D:\\IT\\Programowanie\\testy\\folder do zadan z os\\pliki\\temp\\tyrion_lanister\\quotes.txt',mode='r',encoding='utf-8') as file:
    content = file.readlines()
    print(f'readlines() wyświetlamy listę {content}')

# Iteracja po elementach listy
with open('D:\\IT\\Programowanie\\testy\\folder do zadan z os\\pliki\\temp\\tyrion_lanister\\quotes.txt',mode='r',encoding='utf-8') as file:
    for line in file.readlines():
        print(f'readlines() iterujemy po elementach {content}')

# Iteracja po elementach listy w przypadku dużego pliku, którego nie chcemy otwierać w całości
with open('D:\\IT\\Programowanie\\testy\\folder do zadan z os\\pliki\\temp\\tyrion_lanister\\quotes.txt',mode='r',encoding='utf-8') as file:
    for line in file:
        print(line)

# Podział pliku z wykorzystaniem parametru 'size' funkcji read()
file = open('D:\\IT\\Programowanie\\testy\\folder do zadan z os\\pliki\\temp\\tyrion_lanister\\quotes.txt',mode='r',encoding='utf-8')

fragment = file.read(10)

while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()