# Python sam dopasowuje typ danych
title = 'Python'
print('Title is:',type(title))

version = 3
print('Version is:',type(version))

date = 14.12
print('Date is:',type(date))

# Niektóre zmienne są silniejsze od innych
print('This expression in:',type(version * date))

# Przypisanie kilku zmiennych do jednej wartości
a=b=c=2
print(a,b,c)

# Możemy zmienić wartość jednej ze zmiennych bez wpływu na pozostałe
c = 3
print(a,b,c)

# Obliczenia w pythonie są zgodne z zasadami matematycznymi
print('Result1:',2+2*2)
print('Result2:',6/2*(1+2)) # float ponieważ dzielimy

# Poniższy zapis do 4 do 3 do 2 czyli 4 do 9
print('Result3:',4**3**2)

# Różne sposoby zmiany wartości zmiennych
x = 1
x = x+1
print('x:',x)

x += 1
print('x:',x)

x -= 1
print('x:',x)