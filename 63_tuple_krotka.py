tax = (4, 7, 8, 23) # utworzenie krotki (tuple)
print(tax)

print(tax[2]) # odwołanie do indeksu
print(tax[-1]) # indeksowanie od końca

print(tax.index(7)) # wskaże indeks na którym znajduje się wartość
print(tax.count(8)) # policzy ile razy występuje wartośc przekazana jako argument
print(max(tax)) # przekazujemy krotkę do funkcji max()

tax_list = list(tax) # konwersja krotki na listę
tax_list.append(30) # lista jest mutowalna
print(tax_list)

new_tax = tuple(tax_list) # konwersja listy na krotkę
print(new_tax)

(tax1,tax2,tax3,tax4) = tax # przypisanie wartości z krotki do zmiennych
print(tax1,tax2,tax3,tax4)

a = 1
b = 10
(b,a) = (a,b) # w myśl powyższej zasady zamieniamy wartości zmiennych
print(b,a)

c = 1
d = 10
temp = c # to samo co wyżej tylko przy użyciu zmiennej tymczasowej
c = d
d = temp
print(d,c)