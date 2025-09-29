# Zapisywanie wartości do pliku tekstowego
file_name = r'D:\IT\Programowanie\testy\folder do zadan z os\pliki\temp\output.txt'

line = 'Europe'
cities = ['London','Berlin','Paris','Warsaw','Madrid','Rome']

file = open(file_name,'w')

file.write(line)
file.write('\n')
#file.writelines(cities)

for city in cities:
    file.write(city+'\n')

file.close()

print('====LAB====\n')

print('====ZAD 1====\n')

import os

web_addresses = []

line = input('Enter the web address: ')

while line:
    web_addresses.append(line)
    line = input('Enter next address or press enter: ')

dir_name = os.getcwd()

file_name = input('Enter a file name: ')

file_path = os.path.join(dir_name,file_name)

with open(file_path,'a+') as file:
    for web_addres in web_addresses:
        file.write(web_addres+'\n')

print('====ZAD 2====\n')

user_file = input('Enter path to a file: ')

while not os.path.isfile(user_file):
    user_file = input('Enter the path to an existing file: ')

web_adresses_2 = []

with open(user_file,'r') as file_2:
    for line in file_2.readlines():
        line_no_enter = line.replace('\n','')
        web_adresses_2.append(line_no_enter)

for i in range(len(web_adresses_2)):
    
    text = web_adresses_2[i]
    
    if text.endswith('pl'):
        print(f'Address {text} is from Poland')
    else:
        print(f'Address {text} is not from Poland')