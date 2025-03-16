print('*** Lesson ***\n')

# import modułu
import math

wynik1 = math.ceil(4.2)
print(f'wynik1: {wynik1}')

wynik2 = math.ceil(-3.8) # w górę czyli bliżej zera
print(f'wynik2: {wynik2}')

wynik3 = math.floor(4.7)
print(f'wynik3: {wynik3}')

wynik4 = math.floor(-4.7) # w dół czyli odsuwamy się od 0
print(f'wynik1: {wynik4}')

wynik5 = math.pow(2,8) # math.pow() zwraca typ float
print(f'wynik1: {wynik5}')

wynik6 = math.pow(9,0.5) # podniesienie do potęgi 0.5 to pierwiastek kwadratowy
print(f'wynik1: {wynik6}')

wynik7 = math.sqrt(16)
print(f'wynik1: {wynik7}')

wynik8 = math.sin(math.pi/2)
print(f'wynik1: {wynik8}')

wynik9 = math.cos(math.pi/4)
print(f'wynik1: {wynik9}')

print('\n*** LAB ***')
print('\nTask 1\n')

degree1 = 360
rad1 = degree1 * math.pi / 180
print(rad1)

degree2 = 45
rad2 = degree2 * math.pi / 180
print(rad2)

rad3 = math.radians(360) # konwersja stopni na radiany
rad4 = math.radians(45)
print(rad3,rad4)

print('\nTask 2\n')

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38

small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22.0

# Obliczenie pola powierzchni w metrach kwadratowych 
def circle_area_in_sm(r):
    area_sc = math.pi * math.pow(r,2)
    return round(area_sc / 10000,4)

small_pizza_area = circle_area_in_sm(22)
print(small_pizza_area)

big_pizza_area = circle_area_in_sm(27)
print(big_pizza_area)

family_pizza_area = circle_area_in_sm(38)
print(family_pizza_area)

# Wyznaczenie ceny metra kwadratowego
def sm_price(price,area):
    return price / area

small_sm_cost = sm_price(small_pizza_price, small_pizza_area)
print(f'Metr kwadratowy małej pizzy kosztuje: {round(small_sm_cost,2)} zł')

big_sm_cost = sm_price(big_pizza_price, big_pizza_area)
print(f'Metr kwadratowy małej pizzy kosztuje: {round(big_sm_cost,2)} zł')

family_sm_cost = sm_price(family_pizza_price, family_pizza_area)
print(f'Metr kwadratowy małej pizzy kosztuje: {round(family_sm_cost,2)} zł')

# Pole powierzchni + cena za mater w jednej funkcji
def area_cost(radius,price):
    area_sc = math.pi * math.pow(radius,2)
    area_sm = round(area_sc / 10000,4)
    return price / area_sm

small_sm_cost2 = area_cost(small_pizza_r,small_pizza_price)
print(f'Metr kwadratowy małej pizzy kosztuje: {round(small_sm_cost2,2)} zł')