something_like_number = '1000' # przypisanie do zmiennej liczby w postaci stringa
print(int(something_like_number) + 1) # przekonwertowanie typu string na typ int w celu wykonania działania
print(something_like_number + str(1)) # przekonwertowanie typu int na typ string i wykonanie konkatenacji
print(type(something_like_number)) # funkcja type() zwraca typ danych danego obiektu
print(type(int(something_like_number) + 1)) # zwróci int