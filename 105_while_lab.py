print('\n*** LAB ***')
print('\nTask 1\n')

initial_capital = 20000
percent = 0.03
max_time_years = 10
total_profit = initial_capital
year = 0

while year < max_time_years:
      yeraly_profit = total_profit * percent/100
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

number=20730906
tmpnumber = number
sumOfDigits = 0

while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)