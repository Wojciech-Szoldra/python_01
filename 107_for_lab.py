print('\n*** LAB ***')
print('\nTask 1\n')

fibonacci_iterations = 20
b1 = 0
b2 = 1
b3 = 0

for i in range(0,fibonacci_iterations):
    print(f'Step: {i}, Value: {b3}')
    
    b1 = b2
    b2 = b3
    b3 = b1+b2

print('\nTask 2\n')

text = "Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn't do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it's an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can't."

words = text.split(' ')
    
for word in words:
    if 'p' in word:
        print(f'{word} has letter p')

print('\nTask 3\n')

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'}

for n in dictionary:
    print(f'{n} - {dictionary[n]}')

print('\nTask 3\n')

text = "Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn't do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it's an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can't."

words = text.split(' ')

word_dictionary = {} # Utworzenie słownika {Klucz:Wartość}

for word in words:
    word = word.lower().strip('.,:;!?()[]{}"\'') # Normalizacja słów
    if word in word_dictionary:
        word_dictionary[word] += 1 # Zwiększenie 'wartości' o 1
    else:
        word_dictionary.setdefault(word,1) # Dodanie nowego klucza z wartością
        
print(word_dictionary)