# --Odczyt i kontroli danych wprowadzonych przez użytkownika-- #

# W tym przykładzie string (5) pomnożony zostanie przez liczbę
file_size = input('Enter the max file size (MB): ')
print(f'The max size in KB is {file_size * 1024}')

# Zmienna została przekonwertowana dzięki czemu możemy wykonywać obliczenia
file_size_str = input('Enter the max file size (MB): ')
file_size_int = int(file_size_str)
print(f'The max size in KB is {file_size_int * 1024}')

while True:
    file_size_str = input('Enter the max file size (MB): ')

    if file_size_str.isdecimal():
        file_size_int = int(file_size_str)
        break

print(f'The max size is {file_size_int}')
print(f'The max size in KB is {file_size_int * 1024}')
