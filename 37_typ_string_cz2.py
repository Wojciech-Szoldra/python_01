drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'
path = drive + folder + file # konkatenacja
print(path)

new_text1 = 'text with\nnew line' # znak nowej linii w tekście
print(new_text1)

new_text2 = r'text with\nnew line' # surowy tekst, znaki specjalne są ignorowane
print(new_text2)

# ***38. Typ string cz.2 - LAB***

# Zad 1

firstName = 'Kasia'
famillyName = 'Sowa'
lastName = 'Mrugała'
newName = firstName + ' ' + famillyName + '-' + lastName
print(newName)

# Zad 2

music = '"Universal Fanfare" Jerry Goldsmith, "Happy Together" Garry Bonner, "I\'m a Man" Steve Winwood'
print(music)

# Zad 3

music_new = '"Universal Fanfare" Jerry Goldsmith, \n"Happy Together" Garry Bonner, \n"I\'m a Man" Steve Winwood'
print(music_new)

# Zad 4

line1 = '(\\(\\'
line2 = '( -.-)'
line3 = 'o_(")(")'
print(line1)
print(line2)
print(line3)

all_in_one = '(\\(\\\n( -.-)\no_(")(")'
print(all_in_one)