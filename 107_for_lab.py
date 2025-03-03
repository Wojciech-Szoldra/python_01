print('\n*** LAB ***')
print('\nTask 1\n')

fibonacci_iterations = 20
b1 = 0
b2 = 1
b3 = 0

for i in range(0,fibonacci_iterations):
    print(f'Step: {i}, Value: {b3}')
    
    b1 = b2
    b2 = b3
    b3 = b1+b2