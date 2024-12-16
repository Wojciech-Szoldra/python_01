s = '123456789'
print('Indeks zerowy =',s[0]) # w Pythonie indeksy liczymy od zera
print('Indeks drugi =',s[2])

print('Podzbiór znaków 1=',s[2:7]) # siódmy znak nie jest wyświetlany
print('Podzbiór znaków 2=',s[:8]) # wyświetlone zostaną znaki od pierwszego do siódmego
print('Podzbiór znaków 3=',s[8:]) # wyświetlone zostaną znaki od ósmego do ostatniego
print('Podzbiór znaków 4=',s[2:999]) # Python nie wyrzuci błędu w takiej sytuacji
print('Podzbiór znaków 5=',s[222:10]) # nic nie zostanie wyświetlone

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message[message.find(':')+2:]) # wyświetlamy nazwę drukarki, indeks początkowy wskazuje funkcja find()

# wyświetlamy nazwę dokumentu przy pomocy zmiennej tymczasowej
temp = message[message.find('"')+1:]
print(temp[:temp.find('"')])