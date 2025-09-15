# Funkcja ze słownikiem działająca jak switch

def week_day_in_french(day_number):

	names = {
		0: 'lundi',
		1: 'mardi',
		2: 'mercredi',
		3: 'jeudi',
		4: 'vendredi',
		5: 'samedi',
		6: 'dimanche'
	}

	return names.get(day_number,'error')

print(week_day_in_french(4))
print(week_day_in_french(10))

# Instrukcja match / case dostępna od wersji 3.10

print('*'*40,'\n')

def wykonaj_komende(komenda):
    match komenda:
        case ["idź", kierunek]:
            print(f"Idę w kierunku: {kierunek}")
        case ["weź", przedmiot]:
            print(f"Podnoszę: {przedmiot}")
        case ["wyjdź"]:
            print("Do widzenia!")
        case _:
            print("Nie rozumiem komendy.")

wykonaj_komende(["idź", "północ"])
wykonaj_komende(["weź", "miecz"])
wykonaj_komende(['wyjdź'])
wykonaj_komende(['weź', 'eliksir'])

print('====LAB====\n')

print('====ZAD 1====\n')

# Ciąg geometryczny
# a1-pierwszy element ciągu; factor-iloraz ciągu; index-który element ciągu ma zostać wyliczony

def give_geom_sq_element(a1=2,factor=2,index=2):
     #The function calculates the value of a given term of a geometric sequence
     
	 return a1 * factor**(index-1)

print(give_geom_sq_element(1,2,64))

print('====ZAD 2====\n')

a1 = 3
factor = 2
maxindex = 10

for i in range(1,maxindex+1):
    print(give_geom_sq_element(a1,factor,i))
    
print('====ZAD 3====\n')

def give_factor_for_geom_seq(term,nextterm):
     #The function calculates the factor of two given values
	 
	 return nextterm / term

print(give_factor_for_geom_seq(12,24))

print('====ZAD 4====\n')

def give_sum_of_n_elements_geom_seq(a1=2,factor=2,n=2):
     return a1 * (factor**n -1) / (factor - 1)

print(give_sum_of_n_elements_geom_seq(2,3,4))