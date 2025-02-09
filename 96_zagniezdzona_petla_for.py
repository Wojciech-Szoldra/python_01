print('Lesson')

print('\nver_1\n')

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += ('\t%3d' % (x*y))
    print(line)

print('\nver_2\n')

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += (f'\t{x*y:>3}')
    print(line)