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