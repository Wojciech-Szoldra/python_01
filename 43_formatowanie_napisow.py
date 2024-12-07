message1 = 'Processing file %s' # dołączanie stringa
print(message1 % ('file1.txt'))

message2 = 'File %s has size %d KB' # dołączenie liczby całkowitej int
print(message2 % ('file1.txt',20))

message3 = 'File %20s has size %10d KB' # stała ilość znaków
print(message3 % ('file1.txt',100))

# Drugi sposób formatowania napisów
message4 = 'Processing file {0:s}' # Dołączenie stringa
print(message4.format('file1.txt')) # Parametr przekazujemy do funkcji format

message5 = 'File {0:s} has size {1:d} KB' # Dołączenie stringa i liczby całkowitej
print(message5.format('file1.txt',100))

message6 = 'File {1:s} has size {0:d} KB' # Zmiana kolejności
print(message6.format(100,'File1.txt'))

message7 = 'File {0:20s} has size {1:10d} KB' # Stała ilość znaków
print(message7.format('file1.txt',100))