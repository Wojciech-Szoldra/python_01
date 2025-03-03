print('\n*** LAB ***')
print('\nTask 1\n')

initial_capital = 20000
percent = 0.03
max_time_years = 10
total_profit = initial_capital
year = 0

while year < max_time_years:
      yeraly_profit = total_profit * percent
      total_profit += yeraly_profit
      year += 1
      print(f'Year {year} summary: {round(total_profit, 2)}')

else:
      print(f'Earnings amount: {round((total_profit - initial_capital),2)}')

print('\nTask 2\n')

number = 20730906
sum = 0

print('My approach\n')

sum = 0

while sum <= 0: # Pętla wykona się tylko raz
      number_str = str(number) # konwersja liczby na ciąg znaków
      digits = [int(digit) for digit in number_str] # utworzenie tablicy z cyframi

      for digit in digits:
            sum += digit # Pętla iteruje po cyfrach, a my je sumujemy

      print(sum)

print('\nCourse approach\n')

'''
Podejście zastosowane poniżej:
-> % zwraca resztę z dzielenia - jak dzielimy przez 10 jest to ostatnia cyfra liczby
-> // dzielenie całkowite wykonuje operacje dzielenia i zaokrągla wynik w dół do
   najbliższej liczby całkowitej. Jeżeli dzielimy przez 10 to efekt jest taki, że 'usuwamy' ostatnią cyfrę z liczby.
-> Pętla wykonuje się dopóki tmpnumber > 0, czyli po sunięciu ostatniej cyfry z liczby
   przechodzimy do 'else'.
# ''' 

number=20730906
tmpnumber = number
sumOfDigits = 0

while tmpnumber > 0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)

print('\nTask 3\n')

text = 'United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code-like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier.'

words = text.split(' ')
number_of_words = len(words)
word_length = 6
long_words = 0

for word in words:
     if len(word) > word_length:
          long_words += 1

print(long_words)