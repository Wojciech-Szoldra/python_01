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
   