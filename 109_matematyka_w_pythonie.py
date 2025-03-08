print('---Lesson---\n')

f_smaller = 3.141592653589793
f_bigger = 3.87756392764

print(type(f_smaller))
print('\n')

print(int(f_smaller), int(f_bigger)) # rzutowanie na int
print('\n')

print(abs(f_smaller), abs(-f_smaller)) # funkcja abs() zwraca wartość absolutną
print('\n')

print(round(f_smaller,2),round(f_bigger,2),round(f_bigger,3))
print('\n')

print(min(f_smaller,f_bigger), max(f_smaller, f_bigger))
print('\n')

list=[1,2,3,4,5,4,4,5,4]

print(sum(list)/len(list))
