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

print('====LAB====\n')

print('====ZAD 1====\n')

file_path = r'D:\IT\Programowanie\testy\folder do zadan z os\pliki\temp\data_input\orders.txt'

with open(file_path) as file:
    for line in file:
        line_no_enter = line.replace('\n','')
        line_list = line_no_enter.split(',')
        
        if len(line_list) == 3:
            print(f'Order from drugstore {line_list[0]}, item {line_list[1]}, amount {line_list[2]}')
        else:
            print(f'\n--Line {line_list} incorrect--\n')
    
print('\nProcessing complete.')