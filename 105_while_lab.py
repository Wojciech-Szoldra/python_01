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

number_str = str(number) # konwersja liczby na ciąg znaków

print(number_str)

digits = [int(digit) for digit in number_str] # list comprehension / iterować możemy po stringach

print(digits)

sum = 0

for digit in digits:
    sum += digit
    print(sum)