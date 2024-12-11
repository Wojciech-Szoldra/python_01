x = 30
test1 = x < 30
print(test1)
test2 = not x < 30 # not odwraca wartość logiczną
print(test2)

y = 10
z = 15
test3 = y < 10 and z < 15
print(test3)
test4 = not y < 10 and not z < 15
print(test4)
test5 = not (y < 10 or z < 15)
print(test5)