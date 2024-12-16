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

# *** Napis jako tablica znaków - LAB ***

q = "THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6], sep='')

q = 'a gentelman'
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:], sep='')

q = 'THE MORSE CODE'
print(q[1:3],q[6],q[8:10],q[10:12],q[4],q[2:4],q[12],q[11],q[0],q[7], sep='')

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(':')+2:]
print(time)

tmp = line[line.find('"')+1:]
print(tmp[:tmp.find('"')])