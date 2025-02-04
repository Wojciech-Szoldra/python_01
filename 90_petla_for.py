# Prosta pętla for
owoce = ['jabłko', 'banan', 'wiśnia']

for owoc in owoce:
    print(owoc)

print()

# Poniższa pętla utworzy adresy e-mail dla pracowników znajdujących się w liście, a na
# zakończenie wyświetli komunikat znajdujący się po else.
persons = ['Elizabeth','Steven','Sebastian','Margaret','Svetlana','Raphael']

domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('-- end of the list --')

# *** FOR - LAB ***

print('\n*** LAB ***')
print('\nTask 1\n')

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for dat1 in data:
    print(dat1.upper())

print('\nTask 2\n')

elements = []

for dat2 in data:
    elements = dat2.split(':') # metoda split tworzy listę
    print(elements[0].upper(),elements[1])

print('\nTask 3\n')

for dat2 in data:
    elements = dat2.split(':') # metoda split tworzy listę
    if elements[0] == 'Error':
        print(elements[0].upper(),elements[1].upper())
    else:
        print(elements[0].upper(),elements[1])