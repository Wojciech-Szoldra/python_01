# Algorytm wyszukiwania binarnego

print('Wyszukiwanie binarne\n')

'''
- Lista elementów musi być posortowana
- Jeżeli lista zawiera poszukiwany element zwracana jest informacja o jego położeniu
- Jeżeli nie zawiera elementu zwracany jest Null (czyli None w Pythonie)

while: kod wykonuje się do momentu w którym w liście pozostanie 1 element
    dzielimy (modulo) listę na pół i wynik przypisujemy do 'mid'
    wartość znajdująca się pod indeksem 'mid' przypisana zostaje do 'guess' (to jest liczba którą porównywali będziemy do 'item')

    jeżeli 'guess' == 'item' zwracany jest indeks 'mid'
    
    jeżeli 'guess' > 'item' to do 'high' przypisujemy 'mid-1'. Robimy tak ponieważ wiemy, że środkowa wartość z listy jest większa niż wartość 'item'. Oznacza to, że nie musimy sprawdzać części listy znajdującej się powyżej środkowej wartości, oraz sama środkowa wartość jes różna więc jej też nie musimy sprawdzać (dlatego mid-1)

    w pozostałych przypadkach (guess < item) do low przypisujemy 'mid +1'. Robimy tak ponieważ wiemy, że środkowa wartość z listy jest mniejsza niż wartość 'item'. Oznacza to, że nie musimy sprawdzać części listy znajdującej się poniżej środkowej wartości, oraz sama środkowa wartość jes różna więc jej też nie musimy sprawdzać (dlatego mid+1)
'''

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
        
    return

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, 7))
print(binary_search(my_list, -1))