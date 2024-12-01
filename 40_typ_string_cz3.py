something_like_number = '1000' # przypisanie do zmiennej liczby w postaci stringa
print(int(something_like_number) + 1) # przekonwertowanie typu string na typ int w celu wykonania działania
print(something_like_number + str(1)) # przekonwertowanie typu int na typ string i wykonanie konkatenacji
print(type(something_like_number)) # funkcja type() zwraca typ danych danego obiektu
print(type(int(something_like_number) + 1)) # zwróci int

# *** Typ string cz.3 - LAB ***

article = '''
Monty Python (also collectively known as the Pythons)[2][3] were a British comedy troupe formed in 1969 consisting of Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. The group came to prominence for the sketch comedy series Monty Python's Flying Circus, which aired on the BBC from 1969 to 1974. Their work then developed into a larger collection that included live shows, films, albums, books, and musicals; their influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Their sketch show has been called "an important moment in the evolution of television comedy".[7]
'''

print(article.upper())

print(article.lower().replace('monty','flying'))

# Funkcja count()
word_to_count = 'python' # ustalamy słowo, które ma byc policzone
word_count = article.lower().split().count(word_to_count) # zmniejszamy znaki, tworzymy listę, liczmy
print(f'Słowo "{word_to_count}" występuje {word_count} razy') # wykorzystanie f-string do przedstawienia wyników

# dodałem instrukcję if aby raz/razy dopasowane były do wyniku
print(f'Słowo "{word_to_count}" występuje {word_count} {'razy' if word_count > 1 else 'raz'}') 

# Funkcja count() z łańcuchem znaków
letter_count = 'l'
word = 'umbrella'
print(word.count(letter_count))

print('to print \\ you need to put \\ twice in your text like this: \\\\')

print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")

amount_pln = 234

print('cur\texchange\tamount')
print(f'USD\t3.65\t\t{amount_pln / 3.65}')
print(f'EUR\t4.23\t\t{amount_pln / 4.23}')

value_as_text = '123.45'
factor = 1.23

print(f'value is {value_as_text} factor is {factor} value*factor = {float(value_as_text)*factor}')